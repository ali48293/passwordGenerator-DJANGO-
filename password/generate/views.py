from django.shortcuts import render
import random

def home(request):
    return render(request,"home.html")


def generate(request):
    chars = list("abcdefghijklmnopqrstuvwxyz")
    length=int(request.GET.get('length'))
    if request.GET.get("upper"):
        chars.extend(list("ABCDEFGHIJKLMNOPWRSTUVWXYZ"))
    if request.GET.get("special"):
        chars.extend(list("!@#$%^&*()+;"))
    if request.GET.get("num"):
        chars.extend(list("1234567890"))
            
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return render(request,"generate.html",{"password":password})