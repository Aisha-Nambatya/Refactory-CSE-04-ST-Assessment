from django.shortcuts import render
from .forms import FlightBookingForm



from .forms import FlightBookingForm

def flight_booking(request):
    if request.method == 'POST':
        form = FlightBookingForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = FlightBookingForm()

    return render(request, 'flight_booking.html', {'form': form})

