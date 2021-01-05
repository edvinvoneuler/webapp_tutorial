from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def test_out():
    return HttpResponse('HELLO')
