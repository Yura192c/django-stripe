from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:id>/', views.get_checkout_session_id, name='get_checkout_session_id'),
    path('item/<int:id>/', views.item, name='get_item'),
    path("success/", views.SuccessView.as_view()),
]
