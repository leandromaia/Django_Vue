from django.shortcuts import render
from .forms import TestForm


# Create your views here.
def app1(request):
    return render(request, 'app1.html')


def app2(request):
    return render(request, 'app2.html')


def test(request):
    form = TestForm()

    return render(request, 'test.html', {
        'form': form
    })
