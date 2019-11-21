from django.shortcuts import render, redirect, get_object_or_404

from .models import Venue, Artist, Note, Show, UserProfile
from .forms import VenueSearchForm, NewNoteForm, ArtistSearchForm, UserRegistrationForm, ProfileEditForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.utils import timezone



def user_profile(request, user_pk):
    user = User.objects.get(pk=user_pk)
    userprofile = UserProfile.objects.filter(user=user.pk)
    usernotes = Note.objects.filter(user=user.pk).order_by('posted_date').reverse()
    return render(request, 'lmn/users/user_profile.html', {'user' : user , 'notes' : usernotes, 'profile' : userprofile })


@login_required
<<<<<<< HEAD
def my_user_profile(request, user_pk):

    #user_key = get_object_or_404(UserProfile, pk=user_pk)

    if request.method == 'POST':

        form = ProfileEditForm(request.POST)
        
        if form.is_valid():
            profile = form.save(commit=False)
            #profile.user = request.user
            profile = request.user
            profile.save()
            return redirect('lmn:user_profile', user_pk=request.user.pk)
        else:
            form = ProfileEditForm()
            return render(request, 'lmn/users/my_user_profile.html', { 'form' : form })

    else:
        form = ProfileEditForm()
        return render(request, 'lmn/users/my_user_profile.html', { 'form' : form })
=======
def my_user_profile(request):
    
    if request.method == 'POST':
        
        form = ProfileEditForm(request.POST)
>>>>>>> 770f88d0acb25c66a5f2830cee1d827d1d33110b

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('lmn:user_profile', user_pk=request.user.pk)
    else:
        form = ProfileEditForm()
        return render(request, 'lmn/users/my_user_profile.html', { 'form' : form })


def register(request):

    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            return redirect('lmn:homepage')

        else :
            message = 'Please check the data you entered'
            return render(request, 'registration/register.html', { 'form' : form , 'message' : message } )


    else:
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', { 'form' : form } )
