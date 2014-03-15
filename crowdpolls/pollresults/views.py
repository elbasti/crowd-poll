from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pollresults.forms import LeadForm
# Create your views here.

def index(request):

    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success')
    else:
        form = LeadForm()

    return render(request,'pollresults/home.html', {'form':form})
