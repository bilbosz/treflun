from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def do_register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('login')

    else:
        f = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': f})
