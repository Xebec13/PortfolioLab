from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


class IndexView(View):
    def get(self,request):
        return render(request, "index.html")

class LoginView(View):
    def get(self,request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('index')


class RegisterView(View):
    def get(self,request):
        return render(request, "register.html")

    def post(self,request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            return render(request, "register.html",{'error':'Hasła są nie poprawne'})
        else:
            user = User.objects.create_user(email=email, password=password)
            user.save()
            return render(request, 'index.html')
class AddDonationView(View):
    def get(self,request):
        return render(request, "form.html")