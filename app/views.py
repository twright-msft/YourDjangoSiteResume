﻿"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name' : 'Travis Wright',
    'bio' : 'Software Craftsman',
    'email' : 'radtravis@hotmail.com',
    'twitter_username' : 'radtravis', # No @ symbol, just the handle.
    'github_username' : "twright-msft", 
    'headshot_url' : 'https://s.gravatar.com/avatar/77025c1c3e74b72925fd185303263f2c?s=80', # Link to your GitHub, Twitter, or Gravatar profile image.
}
    
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,    
                'year': datetime.now().year,
            })
    )
