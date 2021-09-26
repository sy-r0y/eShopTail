
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Offer

# "django" is the package, "shortcuts" & "https" are the modules
# we are importing the render() & HttpResponse class
# VIEW FUNCTION generates HTML markup to return back to the client
# VIEW FUNCTION always takes the HTTP request parameter
# index(), connect(), new() etc are the VIEW FUNCTION
# We can use TEMPLATES to show a particular display to the user

# In the TEMPLATE file .. we use {% %} as the TEMPLATE TAG to dynamically execute & evaluate a Python expression
# We use {{ }} as to dynamically insert a value in the HTML markup to be displayed, after Django evaluates the expression


def index(request):

    # show the products in the database to the user & then present it to the user
    # Using TEMPLATES i.e HTML TEMPLATES

    products = Product.objects.all()  # returns all the objects/Products in the referenced class's database i.e Product in this case
    # Product.objects.filter()  # returns the objects in the referenced class which satisfy the filter
    # Product.objects.get()  # getting a single object/product
    # Product.objects.save()  # for saving a new entry
    #response = HttpResponse(products)
    #return response

    # use RENDER() to present the TEMPLATE of the index page defined in the templates directory
    return render(request, 'index.html', {'passed_products': products})
                  # first arg is an object, 2nd is the template file
                  # 3rd argument is a dictionary.. called context
                  # context provides the data to be passed to the template


def offers(request):
    # response = HttpResponse('Offers Page')
    # return response
    offers = Offer.objects.all() # returns ALL objects/offers in the referenced class's database i.e Offer class in this case
    return render(request, 'offers.html', {'offers': offers})

def connect(request):
    response = HttpResponse('Connect Page')
    return response
    # return render(request, 'connect.html')


def new(request):
    response = HttpResponse('New Page')
    return response


def aboutus(request):
    response = HttpResponse("Connect With Us")
    return response


