from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm

# Create your views here.

class profile(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "users/users_profile.html"
    context_object_name = "current_user"

    def get_object(self, queryset=None):
        user = self.request.user
        if user.is_superuser:
            name = f"{user.first_name} {user.last_name}".strip() or user.username
            # Return a default CustomUser or create a default profile if none exists
            custom_user, created = CustomUser.objects.get_or_create(user=user, defaults={
                'name': name,
                'pic': 'no_picture.jpg',
                'bio': 'This is an admin profile.'
            })
            return custom_user
        else:
            # Handle regular users
            return CustomUser.objects.get(user=user)

# function to create a user
def signup_view(request):
    error_message = None
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = None
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1']
                )

                pic = form.cleaned_data['pic']
                if not pic:
                    pic = 'no_picture.jpg'

                customuser = CustomUser(
                    user=user,
                    name=form.cleaned_data['name'],
                    pic=pic,
                    bio=form.cleaned_data['bio']
                )
                customuser.save()

                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
                login(request, user)
                return redirect('users:profile')

            except:
                if user:
                    user.delete()
                error_message = f'Something went wrong. Please try again'
        else:
            error_message = 'Something went wrong.'
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
        'error_message': error_message
    }

    return render(request, 'auth/signup.html', context)