from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from .models import Note
from . import views

@login_required(login_url='/login')
def index(request: HttpRequest):
    notes = Note.objects.filter(owner=request.user)
    return render(
        request, 
        template_name='notes/index.html',
        context={
            "user": request.user,
            "notes": notes
        }
        )

@login_required(login_url='/login')
def add(request: HttpRequest):
    # if HttpRequest.method == 'POST':
    content = request.POST.get('content', '')
    if content != '':
        Note.objects.create(owner=request.user, content=content)
    
    return HttpResponseRedirect(reverse(views.index))

@login_required(login_url='/login')
def detail(request: HttpRequest, note_id: str):
    note = Note.objects.get(pk=note_id)
    return render(request=request, template_name='notes/detail.html', context={"note": note, "owner": request.user})