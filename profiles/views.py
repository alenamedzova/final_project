from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from profiles.models import *


# Create your views here.

@login_required
def profile(request, pk):
    my_profile = UserProfiles.objects.get(id=pk)

    context = {"profile": my_profile}
    return render(request, 'profiles/profile.html', context)


# @login_required
# def create_profile(request):
#     if request.method == 'POST':
#         user = request.user
#         file_url = None
#         if request.FILES.get('avatar'):
#             avatar = request.FILES['avatar']
#             file_storage = FileSystemStorage()
#             file = file_storage.save(avatar.name, avatar)
#             file_url = file_storage.url(file)
#
#         birth_date = request.POST.get('birth_date')
#         if birth_date == "":
#             birth_date = None
#
#         profile = UserProfiles.objects.create(
#             user=user,
#         )
#         user.first_name = request.POST.get('first_name')
#         user.last_name = request.POST.get('last_name')
#         user.email = request.POST.get('email')
#         user.save()
#
#         return redirect('profile', profile.id)
#
#     return render(request, 'profiles/create_profile.html')


@login_required
def edit_profile(request):
    user = request.user
    profile = UserProfiles.objects.get(user=user)

    if request.method == 'POST':
        if request.POST.get('first_name_private'):
            profile.first_name_private = True
        else:
            profile.first_name_private = False
        if request.POST.get('last_name_private'):
            profile.last_name_private = True
        else:
            profile.last_name_private = False
        if request.POST.get('email_private'):
            profile.email_private = True
        else:
            profile.email_private = False

        profile.save()

        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()

        return redirect('profile', profile.id)

    else:
        context = {'profile': profile}
        return render(request, 'profiles/edit_profile.html', context)
