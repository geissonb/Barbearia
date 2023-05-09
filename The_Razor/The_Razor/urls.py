from django.urls import path

from The_Razor.views import IndexTemplateView

app_name = 'The_Razor'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
]
