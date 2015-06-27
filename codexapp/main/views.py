from django.shortcuts import render_to_response, render, redirect

def home(request):

    context = {}

    return render(request, "home.html", context)

