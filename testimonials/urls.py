from django.urls import path
from testimonials import views

urlpatterns = [
    path('testimonials/', views.TestimonialList.as_view()),
    path('testimonials/<int:pk>/', views.TestimonialDetail.as_view()),
]
