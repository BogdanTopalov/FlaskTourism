from werkzeug.exceptions import BadRequest

from db import db
from models import Hotel


class HotelManager:
    @staticmethod
    def get_all_hotels():
        hotels = Hotel.query.all()
        return hotels

    @staticmethod
    def get_single_hotel(hotel_id):
        hotel = Hotel.query.filter_by(id=hotel_id).first()

        if not hotel:
            raise BadRequest(f'Hotel with id:{hotel_id} does not exist')

        return hotel

    @staticmethod
    def add_hotel(hotel_data):
        hotel = Hotel(**hotel_data)

        db.session.add(hotel)
        db.session.flush()
        db.session.commit()

        return hotel

    @staticmethod
    def update_hotel(hotel_id, hotel_data):
        hotel = Hotel.query.filter_by(id=hotel_id).first()

        if not hotel:
            raise BadRequest(f'Hotel with id:{hotel_id} does not exist')

        hotel.name = hotel_data['name']
        hotel.stars = hotel_data['stars']
        hotel.country = hotel_data['country']
        hotel.city = hotel_data['city']
        hotel.image_url = hotel_data['image_url']
        hotel.price_per_night = hotel_data['price_per_night']

        db.session.commit()

        return hotel

    @staticmethod
    def delete_hotel(hotel_id):
        hotel = Hotel.query.filter_by(id=hotel_id).first()

        if not hotel:
            raise BadRequest(f'Hotel with id:{hotel_id} does not exist')

        db.session.delete(hotel)
        db.session.commit()

        return 'Hotel deleted successfully'
