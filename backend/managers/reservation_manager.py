import stripe

from db import db
from managers.auth_manager import auth
from models import Reservation, Hotel, Status


class ReservationManager:
    @staticmethod
    def create_reservation(reservation_data):
        current_user = auth.current_user()
        reservation_data['user_id'] = current_user.id
        reservation = Reservation(**reservation_data)
        hotel = Hotel.query.filter_by(id=reservation.hotel_id).first()
        total_amount = (int(hotel.price_per_night) * 100) * reservation.nights

        try:
            intent = stripe.PaymentIntent.create(
                amount=total_amount,
                currency='bgn',
                payment_method_types=["card"],
                # automatic_payment_methods={
                #     'enabled': True,
                # },
            )
        except Exception:
            intent = None

        db.session.add(reservation)
        db.session.flush()
        db.session.commit()

        if intent:
            return {
                'clientSecret': intent['client_secret'],
                'reservation_id': reservation.id
            }
        return {"reservation_id": reservation.id}

    @staticmethod
    def update_reservation(reservation_id):
        reservation = Reservation.query.filter_by(id=reservation_id).first()
        reservation.status = Status.completed
        db.session.commit()

        return {"message": 'Reservation updated successfully'}

    @staticmethod
    def get_all_reservations():
        reservations = Reservation.query.all()
        return reservations
