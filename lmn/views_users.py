from django.shortcuts import render, redirect
# https://docs.djangoproject.com/en/2.2/ref/contrib/messages/
from django.contrib import messages

from .models import Venue, Artist, Note, Show, UserProfile
from .forms import VenueSearchForm, NewNoteForm, ArtistSearchForm, UserRegistrationForm, UserProfileEditForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.utils import timezone



def user_profile(request, user_pk):
    user = User.objects.get(pk=user_pk)
    #userprofile = UserProfile.objects.get(user=user.pk)
    usernotes = Note.objects.filter(user=user.pk).order_by('posted_date').reverse()
    return render(request, 'lmn/users/user_profile.html', {'user' : user , 'notes' : usernotes })



@login_required
def my_user_profile(request):

    if request.method == 'POST':

        form = UserProfileEditForm(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('lmn:user_profile', user_pk=request.user.pk)
        else:
            messages.error(request, 'Please correct the error')
        
    else:
        form = UserProfileEditForm()

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
