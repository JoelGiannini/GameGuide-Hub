from django.urls import path
from .views import guide_list_view, guide_detail_view

urlpatterns = [
    path('', guide_list_view, name='guide_list'),
    path('<int:pk>/', guide_detail_view, name='guide_detail'),
]
