from django.urls import path
from .views import ProductDetailView, CategoryDetailView, CategoryView, ProductListView, OrderListView, OrderCreateView, ProductCreateView, ConsultationCreateView, ConsultationListView, OrderUpdateView, ConsultationUpdateView

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/create/', ProductCreateView.as_view()),
    path('products/<int:id>/', ProductDetailView.as_view()),
    path('category/', CategoryView.as_view()),
    path('category/<int:id>/', CategoryDetailView.as_view()),
    path('orders/', OrderListView.as_view()),
    path('orders/create/', OrderCreateView.as_view()),
    path('orders/<int:id>/', OrderUpdateView.as_view()),
    path('consultations/create/', ConsultationCreateView.as_view()),
    path('consultations/', ConsultationListView.as_view()),
    path('consultations/<int:id>/', ConsultationUpdateView.as_view())
]
