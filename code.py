from django.db import models
from django.http import HttpReponse

def view(request):
    return HttpReponse("hello python")


def index(request):
    return HttpReponse('index')
