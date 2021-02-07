
from django.urls import path
from . import views
urlpatterns = [
    path('', views.RoomView.as_view(),name = 'RoomView'),
    path('create-room',views.CreateRoomView.as_view(),name = 'CreateRoom'),
    path('get-room',views.GetRoom.as_view(),name = 'GetRoom'),
    path('join-room',views.JoinRoom.as_view(),name = 'JoinRoom'),
    path('user-in-room',views.UserInRoom.as_view(),name = 'UserIn'),
    path('leave-room',views.LeaveRoom.as_view(),name = 'LeaveRoom'),
    path('update-room',views.UpdateRoom.as_view(),name = 'Update'),
]