from flask import request
from flask_restful import Resource

from helpers.decorators import permission_required
from managers.auth_manager import auth
from managers.reservation_manager import ReservationManager
from models.enums import RoleType
from schemas.response.reservations import ReservationResponseSchema


class CreateReservationResource(Resource):
    @auth.login_required
    def post(self):
        data = request.get_json()
        reservation = ReservationManager.create_reservation(data)
        return reservation


class GetAllReservationsResource(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def get(self):
        all_reservations = ReservationManager.get_all_reservations()
        return ReservationResponseSchema(many=True).dump(all_reservations)


class UpdateReservationResource(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def put(self, pk):
        reservation = ReservationManager.update_reservation(pk)
        return reservation
