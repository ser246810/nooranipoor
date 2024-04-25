from django.shortcuts import render
from .models import *

def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        new_message = Message(name=name, email=email, message=message)
        new_message.save()

        return render(request, "main/index.html", {
            "res": "پیام شما با موفقیت ثبت شد"
        })


    return render(request, "main/index.html")