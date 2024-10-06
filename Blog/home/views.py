from django.shortcuts import render
from django.http.request import HttpRequest

# Create your views here.
def render_home(request: HttpRequest):
    if request.method == "POST":
        data = request.POST.dict()
        print(data["message"])
    return render(request, "index.html")