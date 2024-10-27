from http.client import HTTPResponse
from django.shortcuts import render,redirect
from numpy import True_, dtype
import requests
import json
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from request import views as requestsViews
from publish.forms import RideForm
from utils import get_client

client = None
db = None
userDB = None
ridesDB  = None
routesDB  = None

def intializeDB():
    global client, db, userDB, ridesDB, routesDB
    client = get_client()
    db = client.SEProject
    userDB = db.userData
    ridesDB  = db.rides
    routesDB  = db.routes

def search_index(request):
    intializeDB()
    if not request.session.has_key('username'):
        request.session['alert'] = "Please login to create a ride."
        return redirect('index')
    processed = list(ridesDB.find())
    for ride in processed:
        ride['id'] = ride['_id']
    return render(request, 'search/search.html', {"username": request.session['username'], "rides": processed})

def request_ride(request, ride_id):
    """This method processes the request from a user to be part of a ride"""
    intializeDB()

    if not request.session.has_key("username"):
        request.session["alert"] = "Please login to request rides."
        return redirect("index")

    # get ride information from db
    ride = ridesDB.find_one({"_id": ride_id})

    # validation - check for edge cases
    if ride is not None:
        if ride["availability"] == 0:
            message = "Ride has reached max capacity."
        elif ride["owner"] == request.session["username"]:
            message = "Owner of the ride cannot request own rides."
        elif request.session["username"] in ride["confirmed_users"]:
            message = "You are already a confirmed member of this ride."
        else:
            # add/update request to ride
            ridesDB.update_one({"_id": ride_id}, {"$addToSet": {"requested_users": request.session["username"]}})
            message = "Request successful."
        print(message)

    return redirect(requestsViews.requested_rides)

