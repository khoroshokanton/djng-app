from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def news_index(request: HttpRequest):
    return HttpResponse("<h1>Shop</h1>")
