from django.shortcuts import render,redirect
from orders.models import *
from orders.forms import *


# Create your views here.

# orders main page
def orders_reg(request):
    local_list = Local.objects.order_by('date')
    context = {'title': "Register Orders", 'local_list': local_list}

    return render(request, 'orders/order_page.html', context=context)


# for registering a new local order
def new_local(request):
    new_form = LocalForm()

    if request.method == 'POST':
        new_form = LocalForm(request.POST)

        if new_form.is_valid():
            instance = new_form.save(commit=False)

            instance.total_revenue = object.
            print(instance.total_revenue)
            instance.profit = instance.get_profit()
            instance.save(commit=True)
            return redirect('home:home')  # redirect to home page

    context = {'title': "Register Local Order",
               'local_form': new_form}

    return render(request, 'orders/local.html', context=context)


# for registering a new order from South Africa
def new_sa(request):
    context = {'title': "Register South Africa Order"}

    return render(request, 'orders/sa.html', context=context)


# for adding details to an incomplete order
def complete_order(request):
    context = {'title': "Complete an Order"}

    return render(request, 'orders/complete.html', context=context)
