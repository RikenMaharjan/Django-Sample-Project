from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect

from django.views import View
from django.views.decorators.cache import never_cache
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, RedirectView, DetailView

from apps.products.forms import CreateProductForm
from apps.products.models import Product

# Create your views here.
# class View

# mixins, inheritance
def create_product(request):
    form = CreateProductForm()
    if request.method=='POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            form.save()
    elif request.method == 'GET':
        pass

    return render(request, 'backend/create_update/create.html', {'create_form':form})


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [never_cache, login_required]

@method_decorator(decorators, name='post')
class CreateProduct(View):
    template_name = 'backend/create_update/create.html'
    form_class = CreateProductForm
    initial_value = {}

    @method_decorator(decorators)
    def get(self, request):
        form = self.form_class(initial=self.initial_value)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid(): # if it returns true form_valid()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


class UpdateProduct(UpdateView):
    template_name = 'backend/create_update/create.html'
    form_class = CreateProductForm
    model = Product
    #fields = '__all__'
    success_url = '/products/create-cbv/'
    


class DetailProduct(DetailView):
    template_name = 'backend/products/details.html'
    model = Product
    # context_object_name = 'details'
    

def my_view(request):
    if request.method == 'GET':
        return HttpResponse('Result From <h1>function</h1> based view')


class GreetingView(View):
    greeting = "Good Night"

    def get(self, request):
        return HttpResponse(self.greeting)

class MorningGreeting(GreetingView):
    greeting = "Good Morning"


class EveningGreeting(GreetingView):
    greeting = "Good Evening"

    def get(self, request):
        return HttpResponse(f'Hello, {self.greeting}')

