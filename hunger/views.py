from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is where you control the Dino's Hunger Levels</h1>")
