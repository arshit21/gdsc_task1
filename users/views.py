from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request, *args, **kwargs):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			form.save()
			messages.success(request, f'Your Account has been created! You are now able to log in')
			return redirect('index')

	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html',{'form': form})
