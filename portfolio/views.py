from django.shortcuts import render
from .models import Contact,About,Portfolio,We_do
from django.views.generic.edit import FormView
from .forms import ContactForm
from .bot import send_message
from django.views.generic.list import ListView



class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
      name = form.cleaned_data.get('name')
      phone_number = form.cleaned_data.get('phone_number')
      email = form.cleaned_data.get('email')
      content = form.cleaned_data.get('content')
      text = f"Name: {name}\nEmail: {email}\nPhone_number: {phone_number}\ntext: {content}"
      send_message(text)
      print(f"Sending message: {text}")
      Contact.objects.create(
        name=name,
        email=email,
        content=content
    )
      return super().form_valid(form)
    
def home_view(request):
 return render(request=request,template_name='index.html')

# class IndexListView(ListView):
#   model = Index
#   template_name = 'index.html'
#   context_object_name = 'index'
  
class AboutListView(ListView):
  model = About
  template_name = 'about.html'
  context_object_name = 'about'


class PortfolioListView(ListView):
  model = Portfolio
  template_name = 'portfolio.html'
  context_object_name = 'portfolio'


class We_doListView(ListView):
  model = We_do
  template_name = 'we_do.html'
  context_object_name = 'we_do'
