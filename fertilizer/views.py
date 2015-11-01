from django.shortcuts import render, render_to_response, RequestContext
from .forms import fertilizerform, availform #, fertilizeraform
from django.conf import settings

def home(request):
    form = fertilizerform(request.POST)
    avail = availform(request.POST)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    return render_to_response("index.html",
                              locals(),
                              context_instance=RequestContext(request))

def thankyou(request):
    form = fertilizerform(request.POST)
    avail = availform(request.POST)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    return render_to_response("thankyou.html")

def states(request):
    return render_to_response("states.html",
                              locals(),
                              context_instance=RequestContext(request))

def stats(request):
    return render_to_response("stats.html",
                              locals(),
                              context_instance=RequestContext(request))


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
