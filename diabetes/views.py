from django.shortcuts import render


def index(request):
    context = {"status": "Input test results"}
    return render(request, "diabetes/index.html", context)
