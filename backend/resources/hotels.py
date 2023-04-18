from flask import request
from flask_restful import Resource

from helpers.decorators import validate_schema, permission_required
from managers.auth_manager import auth
from managers.hotel_manager import HotelManager
from models import RoleType
from schemas.request.hotels import HotelsRequestSchema
from schemas.response.hotels import HotelResponseSchema


class GetAllHotelsResource(Resource):
    def get(self):
        all_hotels = HotelManager.get_all_hotels()
        return HotelResponseSchema(many=True).dump(all_hotels)


class AddHotelResource(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    @validate_schema(HotelsRequestSchema)
    def post(self):
        data = request.get_json()
        hotel = HotelManager.add_hotel(data)
        return HotelResponseSchema().dump(hotel), 201


class GetHotelResource(Resource):
    @auth.login_required
    def get(self, pk):
        hotel = HotelManager.get_single_hotel(pk)
        return HotelResponseSchema().dump(hotel)


class UpdateHotelResource(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def put(self, pk):
        data = request.get_json()
        hotel = HotelManager.update_hotel(pk, data)
        return HotelResponseSchema().dump(hotel)


class DeleteHotelResource(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def delete(self, pk):
        message = HotelManager.delete_hotel(pk)
        return {"message": message}
