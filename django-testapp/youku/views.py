# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from youku.models import Video

def main_page(request):
    video_list = Video.objects.all()
    return render_to_response('index.html', {'video_list': video_list})
