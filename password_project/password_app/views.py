from django.shortcuts import render
from .forms import PasswordForm
from .utils import generate_passwords, recover_passwords, password_dict
# Create your views here.

def index(request):
    context = {}
    form = PasswordForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        if 'generate' in request.POST:
            key, passwords = generate_passwords(form.cleaned_data)
            context['passwords'] = passwords
            context['key'] = key
            password_dict[key] = passwords
        elif 'recover' in request.POST:
            context['recovered_passwords'] = recover_passwords(form.cleaned_data, password_dict)

    context['form'] = form
    return render(request, 'password_app/index.html', context)
