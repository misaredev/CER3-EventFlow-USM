from django.shortcuts import render

# Create your views here.

def index(request):
    title = "EventFlow"

    data = {
        "title": title,
    }

    return render(request, 'UsmCalendar/index.html', data)