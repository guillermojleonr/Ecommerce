from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("blog/", views.blog_view,name="blog"),
    path("blog/post_categorizados/<int:categoria_id>/", views.post_categorizados,name="post_categorizados"),
]