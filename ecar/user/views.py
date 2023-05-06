from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import AdminRegisterForm,UserRegisterForm
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView
from car.models import *
# Create your views here.

class AdminRegisterView(CreateView):
    model = User
    form_class = AdminRegisterForm
    template_name = 'user/admin_register.html'
    success_url = '/user/home'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)


def home(request):
    return render(request,'user/home.html')

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/user_register.html'
    success_url = '/user/home/'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'user/login.html'
    #form_class = AuthenticationForm
    # success_url ='user/home.html'

    def get_redirect_url(self):
         if self.request.user.is_authenticated:
            if self.request.user.is_admin:
                return '/user/home/'
            else:
                return '/user/base/'

def base(request):
    return render(request,'bas.html')

def base1(request):
    return render(request,'home1.html')

class AdminDashboardView(ListView):

    model = Car
    template_name = 'user/admin_dashboard.html'
    context_object_name = 'car_list' 
  
    # def get(self, request, *args,**kwargs): 
    #     car = Car.objects.all().values()
    #     # cartype = CarType.objects.all().values()
    #     carvarient= CarVarient.objects.all().values()

    #     return render(request, 'user/admin_dashboard.html',{'cars':car})
    # template_name = 'user/admin_dashboard.html'

# class UserDashBoardView(ListView):
    
#     model = User
    
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)
    
    
#     def get_queryset(self):
#         return super().get_queryset()
    
#     template_name = 'user/user_dashboard.html'

def search1(request):
    query = request.GET['query']
    # alllist = Property_info.objects.all()
    alllist = Car.objects.filter(name__contains=query)
    params = {'car_list': alllist}
    return render(request, "car/search1.html" , params)

def about(request):
    return render (request,"user/about.html")

def contact(request):
    return render (request,"user/contact.html")