# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from .serializers import UserSerializer


# class UserListView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         return User.objects.filter(username=self.request.user.username)

# class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         return User.objects.filter(username=self.request.user.username)

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login, authenticate
# from allauth.account.views import LoginView
# from .forms import CustomLoginForm

# class CustomLoginView(LoginView):
#     form_class = CustomLoginForm

#     def form_valid(self, form):
#         role = self.request.POST.get('role')
#         user = authenticate(self.request, username=form.cleaned_data['login'], password=form.cleaned_data['password'])
#         if user is not None:
#             login(self.request, user)
#             if role == 'doctor':
#                 return redirect('doctor-homepage')
#             else:
#                 return redirect('patient-homepage')
#         return super().form_valid(form)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from allauth.account.views import LoginView
from .forms import CustomLoginForm
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomLoginView(LoginView):
    form_class = CustomLoginForm

    def form_valid(self, form):
        role = self.request.POST.get('role')
        user = authenticate(self.request, username=form.cleaned_data['login'], password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
            if role == 'doctor':
                return redirect('doctor-homepage')
            else:
                return redirect('patient-homepage')
        return super().form_valid(form)

@login_required
def doctor_homepage(request):
    return render(request, 'users/doctor_homepage.html')

@login_required
def patient_homepage(request):
    return render(request, 'users/patient_homepage.html')

class UserListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)
