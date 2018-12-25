from django.views.generic import View
from django.shortcuts import get_object_or_404, render, redirect, reverse

from firstapp.models.company import Company
from firstapp.forms.company import CompanyForm, CompanyEditForm


class CompanyView(View):

    def get(self, request):
        if not request.user.is_superuser:
            link = '/products/' + str(request.user.id)
            return redirect(link)
        context = {
            'companies': Company.objects.all(),
            # 'companies': Company.objects.filter(user=request.user),
            'form': CompanyForm()
        }
        return render(request, 'registration/profile.html', context)

    def post(self, request):
        form = CompanyForm(request.POST)
        if form.is_valid():
            user = form.save()
            company = Company(user=user, name=form.cleaned_data['name'])
            company.save()
            return self.get(request)

        context = {
            'companies': Company.objects.all(),
            'form': form
        }
        return render(request, 'registration/profile.html', context)


class CompanyEditView(View):

    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        form = CompanyEditForm(instance=company)
        return render(request, "edit.html", {'form': form})

    def post(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        form = CompanyEditForm(instance=company, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("main_page")
        return render(request, "edit.html", {'form': form})


class CompanyDeleteView(View):

    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        company.delete()
        return redirect('main_page')
