from django.urls import path
from app.views import *
urlpatterns = [
    path('', IndexPage, name="Index"),
    path('blog/', blogHome, name="Blog"),
]
