from django.urls import path
from .views import RealtorsListView, RealtorView, TopSellerView

urlpatterns = [
    path('api/realtors/', RealtorsListView.as_view()),
    path('topseller', TopSellerView.as_view()),
    path('<pk>', RealtorView.as_view()),
]