from django.shortcuts import render,redirect
from .forms import ReserveTableForm
from .models import Reservation


def reserve_table(request):
	
	if request.method == 'POST':
		reserve_form = ReserveTableForm(request.POST)
		if reserve_form.is_valid():
			reserve_form.save()
			return redirect("reservation:reserve_table")
	else:
		reserve_form = ReserveTableForm()

	context = {'form':reserve_form,}
	return render(request,'reservation/reservation.html',context) 