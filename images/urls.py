from django.urls import path
from .views import CalculateHashView, ImageHashListView, ImageHashDetailView

urlpatterns = [
    path('calculate-hash/', CalculateHashView.as_view(), name='calculate-hash'),
    path('image-hashes/', ImageHashListView.as_view(), name='image-hash-list'),
    path('image-hashes/<int:pk>/', ImageHashDetailView.as_view(), name='image-hash-detail'),
]
