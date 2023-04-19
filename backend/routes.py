from resources.auth import RegisterResource, LoginResource
from resources.hotels import GetAllHotelsResource, AddHotelResource,\
    GetHotelResource, UpdateHotelResource, DeleteHotelResource
from resources.reservations import CreateReservationResource, GetAllReservationsResource

routes = (
    (RegisterResource, '/register'),
    (LoginResource, '/login'),
    (GetAllHotelsResource, '/hotels'),
    (AddHotelResource, '/hotels/add'),
    (GetHotelResource, '/hotels/<int:pk>'),
    (UpdateHotelResource, '/hotels/update/<int:pk>'),
    (DeleteHotelResource, '/hotels/delete/<int:pk>'),
    (CreateReservationResource, '/reservations/create'),
    (GetAllReservationsResource, '/reservations')
)
