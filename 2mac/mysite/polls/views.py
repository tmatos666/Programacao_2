from django.template import loader, Template, Context, RequestContext
from django.template.loader import get_template
from django.http import HttpResponseRedirect, HttpResponseNotFound
import sqlite3
from django.shortcuts import redirect,HttpResponse,render
from django import forms
from django.forms import ModelForm


class NameForm(forms.Form):
    album = forms.CharField(label='Album', max_length=100)
    artist = forms.CharField(label='Artist', max_length=100) 
    tracks = forms.CharField( widget=forms.Textarea )

def index(request):
    #variable albumDetails --> return vector of album details 

    #TODO return all album details
    albumDetails = [('1','AC/DC','For Those About To Rock We Salute You')]

    #do not change the lines bellow
    t = get_template('index.html')
    html = t.render({'artists': albumDetails}) 
    return HttpResponse(html)

def read(request, key):
    #variable albumName --> the name of the album for the given key
    #variable tracks --> List of tracks
    #variable artistName --> the name of the artist for the given album

    #TODO return all tracks for the given key of an album
    tracks = [(1,'For Those About To Rock (We Salute You)'),(2,"Let's Get It Up")]
    
    #TODO return the album name of the given key
    albumName = "For Those About To Rock We Salute You"
    
    #TODO return the artist related to a given key of an album
    artistName = "AC/DC"

    #do not change the lines bellow
    t = get_template('read.html')
    html = t.render({'tracks': tracks,'id':key,'name':albumName,'artist':artistName}) 
    return HttpResponse(html)

def create(request):
    #variable albuns --> for instantiating the album class in artistsClass.py
    #variable form.cleaned_data['album'] --> the name of the new album
    #variable form.cleaned_data['artist'] --> the id of the choosed artist
    #Should create a method createAlbum in class Album() in a specific *.py file
      #that inserts a new album in albums table (see database)
      #and returns the key for the new album that will serve to insert the tracks of
      #the new album
    #variable idAlbum --> new id for the new inserted album
    #Should create a method createTracks in class Album() in a specific *.py file
      #that creates the tracks associated to the new album

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            #TODO create a method for inserting a the new album in database 
            # and return the associated key of the new album
            #TODO create a method for inserting the tracks in database for the given 
            # albums

            print(form.cleaned_data['album'])    
            print(form.cleaned_data['artist'])
            print(form.cleaned_data['tracks'].splitlines())

        #do not change the line bellow
        return redirect('index')
    
    allArtists = [(1,'AC/DC'),(2,'Nirvana')]

    #do not change the line bellow
    return render(request, 'create.html', {'artists': allArtists})

def delete(request, key, template_name='delete.html'):
    #variable key --> the id of the album
    #Should create a method deleteAlbum(key) in class Album() in a specific *.py file
      #that delets a new album in albums table (see database)
      #recieving a parameter 'key' corresponding to albumId

    if request.method=='POST':
        #TODO create method for deleting an album for the given key
        print(key)

        #do not change the line bellow
        return redirect('index')

    #do not change the line bellow
    return render(request, template_name)

def update(request, key, template_name='update.html'):
    #variable key --> the id of the album
    #variable form.cleaned_data['album'] --> the name of the album
    #variable form.cleaned_data['artist'] --> the id of the artist
    #Should create a method updateAlbum in class Album() in a specific *.py file
      #should update an album with information given above
    #variable artists --> for instantiating the artists class
    #variable artistName --> for retrieving artist name
    #variable allArtists --> for retrieving all artist
    #variable albumName --> for retrieving album name

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid(): 
            #TODO create method for update an album for the given key
            print(key)
            print(form.cleaned_data['tracks'].splitlines())
            print(form.cleaned_data['album'])
            print(form.cleaned_data['artist'])
            
            #do not change the line bellow
            return redirect('index') 

    #TODO return all tracks for the given key of an album
    tracks = [(1,'For Those About To Rock (We Salute You)'),(2,"Let's Get It Up")]
    #TODO return the album name of the given key
    albumName = "For Those About To Rock We Salute You"
    #TODO return the artist related to a given key of an album
    artistName = "AC/DC"
    allArtists = [(1,'AC/DC'),(2,'Nirvana')]
    
    #do not change the line bellow
    return render(request, template_name, {'tracks':tracks, 'artistName': artistName, 
    'id':key,'albumName': albumName,'artists': allArtists})