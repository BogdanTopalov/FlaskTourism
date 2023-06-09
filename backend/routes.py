from resources.auth import RegisterResource, LoginResource, UserDetailsResource
from resources.hotels import GetAllHotelsResource, AddHotelResource,\
    GetHotelResource, UpdateHotelResource, DeleteHotelResource
from resources.reservations import CreateReservationResource, GetAllReservationsResource, UpdateReservationResource

routes = (
    (RegisterResource, '/register'),
    (LoginResource, '/login'),
    (UserDetailsResource, '/user'),
    (GetAllHotelsResource, '/hotels'),
    (AddHotelResource, '/hotels/add'),
    (GetHotelResource, '/hotels/<int:pk>'),
    (UpdateHotelResource, '/hotels/update/<int:pk>'),
    (DeleteHotelResource, '/hotels/delete/<int:pk>'),
    (CreateReservationResource, '/reservations/create'),
    (GetAllReservationsResource, '/reservations'),
    (UpdateReservationResource, '/reservations/update/<int:pk>')
)
