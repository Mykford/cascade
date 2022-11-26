from django.urls import path
from .views import HomePageView, FullView, NewView, EditView, RemoveView, CategoryView,FullCategoryView
urlpatterns = [
    path('edit/<int:pk>/',EditView.as_view(), name='edit'),
    path('add_category/',CategoryView.as_view(),name='add_category'),
    path('category/<str:category>',FullCategoryView,name='category'),
    path('post/create/',NewView.as_view(),name='create'),
    path('post/<int:pk>/',FullView.as_view(), name='post_detail'),
    path('delete/<int:pk>/',RemoveView.as_view(),name='delete'),
    path('',HomePageView.as_view(), name='home'),
]