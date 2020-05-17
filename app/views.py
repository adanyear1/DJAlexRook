"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact DJ Alex Rook',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About DJ Alex Rook',
            'message':'"Make music that creates a sensation so deep that you forget you are on planet earth"',
            'year':datetime.now().year,
        }
    )

def events(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/events.html',
        {
            'title':'Events',
            'message':'I Look Forward To Seeing You At My Following Events!',
            'year':datetime.now().year,
        }
    )

def gallery(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/gallery.html',
        {
            'title':'Gallery',
            'message':'I invite you to check out my prevous events',
            'year':datetime.now().year,
        }
    )