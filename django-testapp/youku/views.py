# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response

def main_page(request):
    return render_to_response('index.html', None, None)
