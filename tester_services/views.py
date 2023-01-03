from django.shortcuts import render


# Create your views here.
def home(request):
    # return HttpResponse("Home")
    if request.user.is_authenticated:
        status = "You're logged in."
    else:
        status = "You're not logged in."
    context = {'Your Status:': status}
    return render(request, "tester_services/home.html", context)
