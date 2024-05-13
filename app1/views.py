from typing import Any
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserForm





class Registratsiya(View):
    def get(self, request):
        create_form = CustomUserForm()
        context = {
            'form': create_form
        }
        return render(request, 'register.html', context=context)

    def post(self, request):
        create_form = CustomUserForm(data=request.POST, files=request.FILES)
        if create_form.is_valid():
            create_form.save()
            return redirect('app1:login')
        else:
            context = {
                'form': create_form
            }
            return render(request, 'register.html', context=context)


class Login(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {'form': login_form}
        return render(request, 'login.html', context=context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('landing_page')  # Foydalanuvchi muvaffaqiyatli ravishda kirdi, ularni oldin saytga yo'naltiramiz
        else:
            context = {'form': login_form}  # Forma noto'g'ri to'ldirilgan, shu sababli uningni o'zida sahifada qolamiz
            return render(request, 'login.html', context=context)
class LogOut(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        return redirect('landing_page')  



