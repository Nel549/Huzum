from django.shortcuts import render, redirect
from .forms import main_form
from .models import Message
from django.http import HttpResponse
from Agent import file

# Create your views here.

from django.http import JsonResponse
from django.template.loader import render_to_string

def index(request):
    #Message.objects.all().delete()
    last_msg = Message.objects.last()

    form = main_form()
    msgs = Message.objects.all()
    context = {
        'form': form,
        'msgs': msgs,
        'last': msgs
    }
    if request.method == 'POST':
        form = main_form(request.POST)
        msg = request.POST.get('input_msg')

        if form.is_valid():
            form.save()  
            last_msg = Message.objects.last()# create an instance of the form and call save() on it
            output = file.run_api(msg)
            context = {
            'form': form,
            'msgs': msgs,
            'last': output
            }
            


        print(msgs[::-1][0])

    return render(request, 'base/index.html', context)

