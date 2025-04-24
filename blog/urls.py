from django.urls import path
from blog.views import post_list, post_detail, post_add

app_name = "blog"

urlpatterns = [
    path("post_list/", post_list, name="post_list"),
    path("post_add/", post_add, name="post_add"),
    path("<int:post_id>/", post_detail, name="post_detail"),
]