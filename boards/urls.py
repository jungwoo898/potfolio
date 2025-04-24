from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('<str:board_type>/',             views.post_list,   name='post_list'),
    path('<str:board_type>/add/',         views.post_add,    name='post_add'),
    path('<str:board_type>/<int:post_id>/', views.post_detail, name='post_detail'),
]
