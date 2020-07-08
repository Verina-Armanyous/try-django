from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    my_context = {
        "my_num": 12,
        "my_name": "veri",
        "my_list": [12, 33, 2],
    }
    return render(request, "home.html", my_context)
