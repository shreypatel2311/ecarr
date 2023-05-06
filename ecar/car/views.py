from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from .models import *
from .forms import *

# Create your views here.

# <!-- CarType View-->

class CarTypeCreationView(CreateView):
    fields = '__all__'
    model = CarType
    template_name = 'car/cartype_creation.html'
    success_url = '/car/cartype/list/'
    
    def form_valid(self, form):
        return super().form_valid(form)
    
class CarTypeListView(ListView):
    model = CarType
    template_name = 'car/cartype_list.html'
    context_object_name = 'cartype_list'
    
    def get_queryset(self):
        return super().get_queryset()    
    
class CarTypeDeleteView(DeleteView):
    model = CarType
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/car/cartype/list/'

class CarTypeUpdateView(UpdateView):
    model = CarType
    fields = "__all__"
    template_name = 'car/cartype_update.html'
    success_url = '/car/cartype/list/'
    
    def form_valid(self, form):
        return super().form_valid(form)   

class CarTypeDetailView(DetailView):
    model = CarType
    template_name = 'car/cartype_detail.html'
    context_object_name = 'cartype_detail'
     
    def get_queryset(self):
        return super().get_queryset()  
      
    
# <!-- CarVarients View--> 

class CarVarientCreationView(CreateView):
    fields = '__all__'
    model = CarVarient
    template_name = 'car/varient_creation.html'
    success_url = '/car/varient/list/'
    
    
    def form_valid(self, form):
        return super().form_valid(form)
    
class CarVarientListView(ListView):
    model = CarVarient
    template_name = 'car/varient_list.html'
    context_object_name = 'varient_list'
    
    def get_queryset(self):
        return super().get_queryset()    
    
class CarVarientDeleteView(DeleteView):
    model = CarVarient
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/car/varient/list/' 
    
class CarVarientUpdateView(UpdateView):
    fields = "__all__"
    model = CarVarient
    template_name = 'car/varient_update.html'
    success_url = '/car/varient/list/'
    
    def form_valid(self, form):
        return super().form_valid(form)   

class CarVarientDetailView(DetailView):
    model = CarVarient
    template_name = 'car/varient_detail.html'
    context_object_name = 'varient_detail'
    
    def get_queryset(self):
        return super().get_queryset()   
     

# <!-- CarEngine View -->

class CarEngineAndTransmissionCreationView(CreateView):
    fields = '__all__'
    model = CarEngineAndTransmission
    template_name = 'car/engine_creation.html'
    success_url = '/car/engine/list/'
    
    def form_valid(self, form):
        return super().form_valid(form)
    
class CarEngineAndTransmissionListView(ListView):
    model = CarEngineAndTransmission
    template_name = 'car/engine_list.html'
    context_object_name = 'engine_list'
    
    def get_queryset(self):
        return super().get_queryset()    
    
class CarEngineAndTransmissionDeleteView(DeleteView):
    model = CarEngineAndTransmission
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/car/engine/list/'

class CarEngineAndTransmissionUpdateView(UpdateView):
    fields = "__all__"
    model = CarEngineAndTransmission
    template_name = 'car/engine_update.html'
    success_url = '/car/engine/list/'
    
    def form_valid(self, form):
        return super().form_valid(form)   

class CarEngineAndTransmissionDetailView(DetailView):
    model = CarEngineAndTransmission
    template_name = 'car/engine_detail.html'
    context_object_name = 'engine_detail'
    
    def get_queryset(self):
        return super().get_queryset()    
    

# <!-- CarBrand View -->

class BrandCreationView(CreateView):
    fields = '__all__'
    model = Brand
    template_name = 'car/brand_creation.html'
    success_url = '/car/brand/list/'

    def form_valid(self, form):
        return super().form_valid(form)
    
class BrandListView(ListView):
    model = Brand
    template_name = 'car/brand_list.html'
    context_object_name = 'brand_list'
    
    def get_queryset(self):
        return super().get_queryset()
    
class BrandDeleteView(DeleteView):
    model = Brand
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/car/brand/list/'

class BrandUpdateView(UpdateView):
    fields = '__all__'
    model = Brand
    template_name = 'car/brand_update.html'
    success_url = '/car/brand/list/'
    
    def form_valid(self, form):  
        return super().form_valid(form)   

class BrandDetailView(DetailView):
    model = Brand
    template_name = 'car/brand_detail.html'
    context_object_name = 'brand_detail'
    
    def get_queryset(self):
        return super().get_queryset()


# <!-- Fuel View -->

class FuelCreationView(CreateView):
    fields = '__all__'
    model = Fuel
    template_name = 'car/fuel_creation.html'
    success_url = '/car/fuel/list/'

    def form_valid(self, form):
        return super().form_valid(form)
    
class FuelListView(ListView):
    model = Fuel
    template_name = 'car/fuel_list.html'
    context_object_name = 'fuel_list'
    
    def get_queryset(self):
        return super().get_queryset()
    
class FuelDeleteView(DeleteView):
    model = Fuel
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/car/fuel/list/'

class FuelUpdateView(UpdateView):
    fields = '__all__'
    model = Fuel
    template_name = 'car/fuel_update.html'
    success_url = '/car/fuel/list/'
    
    def form_valid(self, form):  
        return super().form_valid(form)   

class FuelDetailView(DetailView):
    model = Fuel
    template_name = 'car/fuel_detail.html'
    context_object_name = 'fuel_detail'
    
    def get_queryset(self):
        return super().get_queryset()


# <!-- Exterior View -->

class ExteriorCreationView(CreateView):
    fields = '__all__'
    model = Exterior
    template_name = 'car/exterior_creation.html'
    success_url = '/car/exterior/list/'

    def form_valid(self, form):
        return super().form_valid(form)
    
class ExteriorListView(ListView):
    model = Exterior
    template_name = 'car/exterior_list.html'
    context_object_name = 'exterior_list'
    
    def get_queryset(self):
        return super().get_queryset()
    
class ExteriorDeleteView(DeleteView):
    model = Exterior
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/car/exterior/list/'

class ExteriorUpdateView(UpdateView):
    fields = '__all__'
    model = Exterior
    template_name = 'car/exterior_update.html'
    success_url = '/car/exterior/list/'
    
    def form_valid(self, form):  
        return super().form_valid(form)   

class ExteriorDetailView(DetailView):
    model = Exterior
    template_name = 'car/exterior_detail.html'
    context_object_name = 'exterior_detail'
    
    def get_queryset(self):
        return super().get_queryset()    
    
    
# <!-- CarView -->

class CarCreationView(CreateView):
    form_class = CarCreationForm
    model = Car
    template_name = 'car/car_creation.html'
    success_url = '/car/car/list/'

    def form_valid(self, form):
        return super().form_valid(form)
    
class CarListView(ListView):
    model = Car
    template_name = 'car/car_list.html'
    context_object_name = 'car_list'
    
    def get_queryset(self):
        return super().get_queryset()
   
    # def get(self, request, *args,**kwargs): 
    #     car = Car.objects.all().values()
        # cartype = CarType.objects.all().values()
        # carvarient= CarVarient.objects.all().values()

    #     return render(request, 'car/carlist.html',{'cars':car})
    # template_name = 'car/carlist.html' 
    
class CarDeleteView(DeleteView):
    model = Car
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/user/admin/dashboard/'

class CarUpdateView(UpdateView):
    form_class = CarCreationForm
    model = Car
    template_name = 'car/car_update.html'
    success_url = '/car/car/list/'
    
    def form_valid(self, form):  
        return super().form_valid(form)   

class CarDetailView(DetailView):
    model = Car
    template_name = 'car/car_detail2.html'
    context_object_name = 'car_detail'
    
    def get_queryset(self):
        return super().get_queryset()    
    # def get(self, request, *args,**kwargs): 
    #     car = Car.objects.all().values()
    #     return render(request, 'car/car_detail.html',{'cars':car})
    # template_name = 'car/car_detail.html'

def search(request):
    cars = Car.objects.all()

    data = {
        'cars': cars,
        # 'model_search': model_search,
        # 'year_search': year_search,
        # 'body_style_search': body_style_search,
        # 'brand_search': brand_search,
    }
    return render(request, 'car/search.html', data)


def home(request):
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.all().order_by('-created_date')
    data = {
        'featured_cars': featured_cars,
        'all_cars': all_cars,
    }
    return render(request, 'home1.html', data)
     