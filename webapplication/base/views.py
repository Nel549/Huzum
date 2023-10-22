from django.shortcuts import render, redirect
from .forms import main_form
from .models import Message
from django.http import HttpResponse

# Create your views here.

from django.http import JsonResponse
from django.template.loader import render_to_string

def index(request):
    form = main_form()
    context = {
        'form': form,
        'msgs': Message.objects.all()
    }
    if request.method == 'POST':
        form = main_form(request.POST)
        msg = request.POST.get('input_msg')

        if form.is_valid():
            form.save()  # create an instance of the form and call save() on it
            data = {
                'msg': msg,
                'class': 'left-msg'
            }
            html = render_to_string('base/message.html', {'data': data})
            return JsonResponse({'html': html})

    return render(request, 'base/index.html', context)

