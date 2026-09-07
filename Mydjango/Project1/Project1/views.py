from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound
from django.views.decorators.http import require_http_methods
@require_http_methods(["GET"])
def hello(request):
    return HttpResponse("<h1>Hello,Welcome to Django!</h1>")

@require_http_methods(["GET"])
def showcollege(request):
    return HttpResponse("<h1><center>Meerut Institue of Technology</center></h1><BR><Marquee bgcolor='Pink' size=5>New Admission Going On</Marquee>")
@require_http_methods(["GET"])

def showschedule(request):
    return render(request, 'schedule.html')

@require_http_methods(["GET"])
def hotel(request):
    return render(request, 'hotel.html')
