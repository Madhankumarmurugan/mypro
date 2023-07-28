
from django.db.models.query import QuerySet
from django.shortcuts import render
from M5app.models import userimg
from django.views.generic import ListView,DetailView
from django.db.models import Q


# Create your views here.
class display(ListView):
    queryset=userimg.objects.all()
    template_name='M5app/img.html'


class Petshop(DetailView):
      #model=userimg
      queryset=userimg.objects.all()
      template_name = "M5app/petdetail.html"

def get_context_data(self,*args,**kwargs):
    context = super(Petshop,self).get_context_data(self,*args, **kwargs)
    return context
 
class search(ListView):
     model=userimg
     template_name='M5app/nav.html'

     def get_queryset(self):
          query=self.request.GET.get('search')
          object_list=userimg.objects.filter(Q(name__icontains=query) | Q(age__icontains=query))
          return object_list


          
   
    

     
     
