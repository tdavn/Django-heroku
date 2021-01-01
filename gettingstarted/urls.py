from django.urls import path, include

from django.contrib import admin
from blog.views import AddPostView, UpdatePostView, DeletePostView
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('members/', include('django.contrib.auth.urls')),  # This one for django system
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('members/', include('members.urls')),  # This one will be defined in app's urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
