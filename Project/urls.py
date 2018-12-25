from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path, include
from firstapp.views.company import CompanyView, CompanyEditView, CompanyDeleteView
from firstapp.views.product import ProductView, EditProductView, DeleteProductView


urlpatterns = [
    path('', login_required(CompanyView.as_view()), name='main_page'),

    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^admin/', admin.site.urls),

    path('edit/<int:company_id>/', login_required(CompanyEditView.as_view()), name='company_edit'),
    path('delete/<int:company_id>/', login_required(CompanyDeleteView.as_view()), name='company_delete'),

    path('products/<int:company_id>/', login_required(ProductView.as_view()), name='products_list'),
    path('products/<int:company_id>/edit/<int:product_id>/', login_required(EditProductView.as_view()), name='product_edit'),
    path('products/<int:company_id>/delete/<int:product_id>/', login_required(DeleteProductView.as_view()), name='product_delete'),
]
