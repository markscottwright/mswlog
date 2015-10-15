from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from callog.models import WeighIn
from callog.forms import WeighInForm


@login_required
def overview(request):
    return HttpResponse("hello")


def user_info(request):
    return HttpResponse(str(request.user))


@login_required
def weigh_ins(request):
    if request.method == 'POST':
        form = WeighInForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/callog/weighins")
    else:
        form = WeighInForm()

    weigh_in_entries = WeighIn.objects.all()
    return render(
        request, 'weighins.html', {
            'weigh_ins': weigh_in_entries,
            'form': form,
            })
