from django.shortcuts import render, redirect
from .forms import main_form
from .models import Message

# Create your views here.

def index(request):
    form = main_form()
    #Message.objects.all().delete()
    context = {
        'form': form,
        'msgs': Message.objects.all()
    }
    if request.method == 'POST':
        form = main_form(request.POST)
        #msg = request.POST.get('input_msg')

        if form.is_valid():
            main_form.save()
            return redirect(' ')



    return render(request, 'base/index.html', context)

