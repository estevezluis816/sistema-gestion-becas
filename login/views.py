from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, 'Debes completar todos los campos.')
            return render(request, 'login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser and user.is_active:
            django_login(request, user)
            return redirect('inicio')  # Redirige al inicio si el login es correcto
        else:
            messages.error(request, 'Credenciales inválidas o usuario no autorizado.')
            return render(request, 'login.html')

    return render(request, 'login.html')
