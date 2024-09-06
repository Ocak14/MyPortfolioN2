from django.urls import path
from .views import home_view,  ContactFormView, AboutListView,PortfolioListView,We_doListView, ContactFormView


urlpatterns = [
     path('',home_view,name='index-page'),
    path('about/',AboutListView.as_view(),name='about-page'),
    path('contact/', ContactFormView.as_view(), name='contact-page'),
    path('portfolio/',PortfolioListView.as_view(),name='portfolio-page'),
    path('we_do/',We_doListView.as_view(),name='we_do-page'),

]