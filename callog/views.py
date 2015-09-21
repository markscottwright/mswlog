from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def overview(request):
    return HttpResponse("hello")


def user_info(request):
    return HttpResponse(str(request.user))
