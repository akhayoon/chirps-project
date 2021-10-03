from django.urls import include, path
from django.conf.urls import url
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('chirps/', views.ChirpsHandler.as_view()),
]