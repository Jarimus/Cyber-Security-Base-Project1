# from django.shortcuts import render
from django.http import HttpResponse

def HomePageView(request):
    return HttpResponse("""
<h1>Hi!</h1>
                        
<p>This is my website that I'm building</p>
                        
<p>The idea is the learn sum djangky skillz</p>""")

def PingView(request):
    return HttpResponse('You pinged the server')

def TestView(request):
    return HttpResponse('Testing how routes work')