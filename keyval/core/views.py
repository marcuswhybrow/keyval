from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.http import Http404
from keyval.core.models import KeyVal
from django.template import RequestContext

def user_profile(request, username):
    """Displays the key value pairs for a user"""
    
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404
    
    return render_to_response('core/user_profile.html', {
        'user_profile': user,
    }, context_instance=RequestContext(request))

def keyval_profile(request, username, key):
    """Displays information regarding a key for the given username"""
    
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404
    
    try:
        keyval = KeyVal.objects.get(key=key)
    except KeyVal.DoesNotExist:
        raise Http404
    
    return render_to_response('core/keyval_profile.html', {
        'user_profile': user,
        'keyval': keyval,
    }, context_instance=RequestContext(request))