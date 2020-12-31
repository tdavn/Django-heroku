from django.urls import path
from . import views
from .views import AddPostView

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
    # path('add_post/', AddPostView.as_view(), name='add_post'),
]
