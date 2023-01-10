from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from test_generator.models import *


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        status = "You're currently logged in."
    else:
        status = "You're not currently logged in."
    context = {'status': status}
    return render(request, "tester_services/home.html", context)


# môže sa neskôr zmazať (def testujeme)
def testujeme(request):
    thema = Themes.objects.create(theme_name="Biology")


@login_required
def my_tests(request):
    user = request.user
    tests = GTest.objects.filter(user_id=user.id)
    context = {'my_tests': tests}
    return render(request, 'tester_services/my_tests.html', context)

