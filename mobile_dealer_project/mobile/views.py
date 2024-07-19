from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Mobile
from .forms import MobileForm, BuyMobileForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
def add_mobile(request):
    if request.method == 'POST':
        form = MobileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mobile_list')
    else:
        form = MobileForm()
    
    return render(request, 'mobile/add_mobile.html', {'form': form})

def mobile_list(request):
    mobiles = Mobile.objects.all()
    return render(request, 'mobile/mobile_list.html', {'mobiles': mobiles})

def buy_mobile(request):
    if request.method == 'POST':
        name = request.POST.get('mobile_name')
        brand = request.POST.get('mobile_brand')
        price = request.POST.get('mobile_price')
        
        mobiles = Mobile.objects.filter(name=name, brand=brand, price=price, quantity__gt=0).order_by('id')
        if mobiles:
            mobile_to_update = mobiles.first()
            if mobile_to_update.quantity > 0:
                mobile_to_update.quantity -= 1
                mobile_to_update.save()
                return render(request, 'mobile/buy_mobile.html', {'mobiles': get_combined_mobiles(), 'success': f"You bought {mobile_to_update.name}!"})
        
        return render(request, 'mobile/buy_mobile.html', {'mobiles': get_combined_mobiles(), 'error': 'Out of stock'})

    # GET request
    return render(request, 'mobile/buy_mobile.html', {'mobiles': get_combined_mobiles()})

def get_combined_mobiles():
    mobiles = Mobile.objects.values('name', 'brand', 'price').annotate(total_quantity=Sum('quantity'))
    return mobiles