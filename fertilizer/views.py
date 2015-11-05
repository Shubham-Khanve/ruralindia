from django.shortcuts import render, render_to_response, RequestContext
from .forms import nameform, emailform, passwordform #, fertilizeraform
from django.conf import settings

def home(request):
    return render_to_response("index.html",
                              locals(),
                              context_instance=RequestContext(request))

def states(request):
    return render_to_response("states.html",
                              locals(),
                              context_instance=RequestContext(request))

def stats(request):
    return render_to_response("stats.html",
                              locals(),
                              context_instance=RequestContext(request))

def register(request):
    name = nameform(request.POST)
    email = emailform(request.POST)
    password = passwordform(request.POST)
    return render_to_response("register.html",
                              locals(),
                              context_instance=RequestContext(request))

def thankyou(request):
    name = nameform(request.POST)
    email = emailform(request.POST)
    password = passwordform(request.POST)
    return render_to_response("thankyou.html")


#def zero(request):
#    form = fertilizerform(request.POST or None)
#    if form.is_valid():
 #       save_it = form.save(commit=False)
 #       save_it.save()
 #   return render_to_response("indexa.html")

#def zeroa(request):
 #   form = fertilizeraform(request.POST or None)
 #   if form.is_valid():
 #       save_it = form.save(commit=False)
 #       save_it.save()
 #   return render_to_response("indexa.html",
 #                             locals(),
 #                             context_instance=RequestContext(request))

#def contact(request):
    
   # return render_to_response("contact.html",
                      #        locals(),
                       #       context_instance=RequestContext(request)).yki8hy;9;y0bhi8yg
   # return render_to_response("pricing.html",
                      #        locals(),
                      #        context_instance=RequestContext(request))

# Create your views here.
