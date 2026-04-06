from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.db import connection
from .models import Note


@login_required(login_url='/login')
def index(request: HttpRequest):
    search_term = request.GET.get("search_term", "")
    user = request.user

    # FIX FLAW 1: Comment out this query (lines 16-22)
    with connection.cursor() as cursor:
        cursor.execute(f"""
SELECT a.username, n.content, n.id FROM notes_note n
    LEFT JOIN auth_user a ON a.id = n.owner_id
WHERE n.content LIKE '%{search_term}%' AND a.username = '{user}';""")
        results = cursor.fetchall()
        notes = [ {"owner": r[0], "content": r[1], "pk": r[2]} for r in results ]

    # FIX FLAW 1: Include this query with the search term (lines 25-27)
    # notes = Note.objects.filter(owner=request.user)
    # if search_term != "":
    #     notes = notes.filter(content__contains=search_term)

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
    content = request.POST.get('content', '')
    if content != '':
        Note.objects.create(owner=request.user, content=content)
    
    return HttpResponseRedirect(reverse(index))


@login_required(login_url='/login')
def delete(request: HttpRequest, note_id: str):
    note = Note.objects.get(pk=note_id)
    if note.owner == request.user:
        note.delete()
        return HttpResponseRedirect(reverse(index))
    else:
        return HttpResponseForbidden()


# FLAW 2: Login is not required to access certain pages
# FLAW 2 FIX: Include the @login_required decorator
# @login_required(login_url='/login')
def detail(request: HttpRequest, note_id: str):

    note = Note.objects.get(pk=note_id)

    if request.method == "DELETE":
        note.delete()
        return HttpResponseRedirect(redirect_to='/')

    # FIX FLAW 2: Include this to ensure the logged in user is the owner of the note.
    # if note.owner != request.user:
    #     return HttpResponseForbidden()
    return render(request=request, template_name='notes/detail.html', context={"note": note, "owner": note.owner})



def register(request: HttpRequest):
    if request.method != "POST":
        return render(request=request, template_name='notes/register.html', context={})
    username = request.POST.get("username", "")
    password1 = request.POST.get("password", "")
    password2 = request.POST.get("confirm_password", "")
    if username == "" or password1 == "" or password2 == "":
        return render(request=request, template_name='notes/register.html', context={"error_message": "Please provide a username and a password."})
    if password1 != password2:
        return render(request=request, template_name='notes/register.html', context={"error_message": "Passwords did not match."})
    User.objects.create_user(username=username, password=password1)
    return HttpResponseRedirect(redirect_to="/")