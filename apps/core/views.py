from django.shortcuts import render

from .forms import SampleForm


# Create your views here.
def home(request):
    return render(request, "base.html")


def forms(request):
    form = SampleForm()
    context = {"form": form}
    return render(request, "forms.html", context)
