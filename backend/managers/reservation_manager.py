from db import db
from managers.auth_manager import auth
from models import Reservation


class ReservationManager:
    @staticmethod
    def create_reservation(reservation_data):
        current_user = auth.current_user()
        reservation_data['user_id'] = current_user.id
        reservation = Reservation(**reservation_data)

        db.session.add(reservation)
        db.session.flush()
        db.session.commit()

        return reservation

    @staticmethod
    def get_all_reservations():
        reservations = Reservation.query.all()
        return reservations
