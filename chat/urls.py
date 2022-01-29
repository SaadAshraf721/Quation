from django.urls import path

from chat.views import *

urlpatterns = [
    path('chatre/<int:id>/', chatre),
    path('com', com, name='com'),
    path('receive_data/<int:uid>/<int:pid>/', receive_data, name='receive_dataa'),
    path('chatrea/<int:id>/', chatrea),
    path('coma', coma, name='com'),
    path('receive_dataa/<int:uid>/<int:pid>/', receive_dataa, name='receive_dataa'),
]
