from http.client import HTTPResponse
from django.shortcuts import render,redirect
from numpy import True_, dtype
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
        if request.session['username'] != ride['owner'] and ride['availability'] > 0:
            ride['allow_to_join'] = True
    return render(request, 'search/search.html', {"username": request.session['username'], "rides": processed})

def join_ride(request,ride_id):
    if not request.session.has_key('username'):
        request.session['alert'] = "Please login to create a ride."
        return redirect('index')
    #username has requested to join the ride 
    #pull out the ride from db 
    intializeDB()
    query = {"_id": ride_id}
    update = {"$push": {"requested_users": request.session['username']}}
    ridesDB.update_one(query,update)
    return render(request, 'home/home.html', {"username": request.session["username"]})