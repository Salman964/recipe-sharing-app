# user/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.models import User

@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'user/user_profile.html', {'profile': profile})

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)

    # Check if the user is already following the target user
    if request.user.userprofile.following.filter(pk=user_to_follow.userprofile.pk).exists():
        # Unfollow the user
        request.user.userprofile.following.remove(user_to_follow.userprofile)
    else:
        # Follow the user
        request.user.userprofile.following.add(user_to_follow.userprofile)

    # Redirect to the user profile page
    return redirect('user:user_profile', username=username)
