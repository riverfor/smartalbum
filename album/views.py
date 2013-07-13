"""
    Album Views

"""

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import User,Photo

def home(request):
    """
        List all users
    """
    my_data = { 'users': User.objects.all() } 
    return render_to_response('album/home.html',
                              my_data,
                              context_instance=RequestContext(request))

def detail(request, uid):
    user = User.objects.get(id=uid)
    my_data = { 'photos': Photo.objects.filter(user_id=uid), 'user_name': user.display_name } 
    return render_to_response('album/detail.html',
                              my_data,
                              context_instance=RequestContext(request))

