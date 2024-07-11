from django.shortcuts import render
from . import models
from .models import Destination
# Create your views here.

def index(request):
    
    # as we have connected the data base postgre SQL and django with psycopg2
    # next, we define the models which are used to created the tables in the postgre sql database using ORM.
    # as the database is connected, the function, method, code in order to fetch the data,rows from the database is Destination(model,class, table). objects.all()
    dests = Destination.objects.all() # this .objects.all() is to give or return all the rows in the table destination
    return render(request, 'index.html', {'dests':dests})
