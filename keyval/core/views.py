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
        keyval = KeyVal.objects.get(key=key, user=user)
    except KeyVal.DoesNotExist:
        raise Http404
    
    return render_to_response('core/keyval_profile.html', {
        'user_profile': user,
        'keyval': keyval,
    }, context_instance=RequestContext(request))

from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def keyval_edit(request, username, key):
    """Allows editing of keyvals if the logged in user owns the keyval"""
    
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise  Http404
    
    try:
        keyval = KeyVal.objects.get(key=key, user=user)
    except KeyVal.DoesNotExist:
        raise Http404
    
    if user != request.user:
        raise Http404
    
    if request.method == 'POST':
        value = request.POST.get('value', keyval.value)
        keyval.value = value
        keyval.save()
        
        messages.success(request, 'Your keyval information has been updated.')
    
    return render_to_response('core/keyval_edit.html', {
        'keyval': keyval,
    }, context_instance=RequestContext(request))
        

@login_required
def account(request):
    """Displays information about the users account"""
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name', request.user.first_name)
        last_name = request.POST.get('last_name', request.user.last_name)
        email = request.POST.get('email', request.user.email)
        
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.email = email
        request.user.save()
        
        messages.success(request, 'Your account information has been updated.')
    
    return render_to_response('core/account.html', context_instance=RequestContext(request))

def index(request):
    """Displays standard welcome page, or user home page if logged in"""
    
    if request.user.is_authenticated():
        template = 'core/authenticated.html'
    else:
        template = 'core/index.html'
    
    return render_to_response(template, context_instance=RequestContext(request))