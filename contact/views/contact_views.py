# flake8: noqa
from typing import Any, Dict
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q

# Create your views here.


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    context = {
        'page_object': page_object,
        'site_title': 'Contacts - '
    }

    return render(request, 'contact/index.html', context)


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects.filter(show=True).filter(
        Q(email__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value)).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    context = {
        'page_object': page_object,
        'site_title': 'Search - ',
        'search_value': search_value
    }

    return render(request, 'contact/index.html', context)


def contact(request, contact_id):
    single_contact = get_object_or_404(
        Contact.objects.filter(pk=contact_id), show=True)

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title
    }

    return render(request, 'contact/contact.html', context)
