from django.urls import path
from .views import BlogListView, BlogDetailView,BlogCeateView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCeateView.as_view(), name='post_new')

]
