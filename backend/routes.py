from resources.auth import RegisterResource, LoginResource
from resources.hotels import GetAllHotelsResource, AddHotelResource,\
    GetHotelResource, UpdateHotelResource, DeleteHotelResource


routes = (
    (RegisterResource, '/register'),
    (LoginResource, '/login'),
    (GetAllHotelsResource, '/hotels'),
    (AddHotelResource, '/hotels/add'),
    (GetHotelResource, '/hotels/<int:pk>'),
    (UpdateHotelResource, '/hotels/update/<int:pk>'),
    (DeleteHotelResource, '/hotels/delete/<int:pk>')
)
