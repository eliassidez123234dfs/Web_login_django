from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


def catalogue(request):
    return render(request, 'products/catalogue.html')


@staff_member_required
def admin_panel(request):
    return render(request, 'products/admin_panel.html')
