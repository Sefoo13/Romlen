from django.http import HttpResponseNotFound
from django.views.generic import View
from django.shortcuts import get_object_or_404, render, redirect, reverse


from firstapp.models import Company, Product
from firstapp.forms.product import ProductForm


class ProductView(View):

    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        # if request.user != company.user:
        #     return HttpResponseNotFound('<h1>Page not found</h1>')

        context = {
            'company': company,
            'form': ProductForm(initial={'company': company})
        }
        return render(request, "list_products.html", context)

    def post(self, request, company_id):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return self.get(request, company_id)
        context = {
            'company': get_object_or_404(Company, pk=company_id),
            'form': form
        }

        return render(request, "list_products.html", context)


class EditProductView(View):
    def get(self, request, company_id, product_id):
        product = get_object_or_404(Product, pk=product_id)
        form = ProductForm(instance=product)
        return render(request, "list_products.html", {'form': form})

    def post(self, request, company_id, product_id):
        product = get_object_or_404(Product, pk=product_id)
        form = ProductForm(instance=product, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_list', company_id)

        return render(request, "list_products.html", {'form': form})


class DeleteProductView(View):

    def get(self, request, company_id, product_id):
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        return redirect('products_list', company_id)
