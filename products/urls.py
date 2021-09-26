

# urls.py MODULE is used to map url to functions
# URL MAPPING
# urls.py is used to MAP the URL request to their VIEW FUNCTION to provide a response

from django.urls import path
from . import views

# import views   # do not do this .. cuz views is GENERIC & other libraries may also have views module
# from products import views

# urlpatterns is a convention & is a list object
urlpatterns = [

    path('', views.index),  # views.index is a reference to the index()
    # empty string '' represents the ROOT of our app
    # views.index is a reference to the index(). we are NOT calling the function here
    # index is NOT called here as Django would call it on its own at RUNTIME
    path('connect/', views.connect),
    path('new/', views.new),
    path('connect/aboutus', views.aboutus),
    path('offers/', views.offers)
]