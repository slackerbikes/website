from django.shortcuts import render
from events.forms import BookingForm
from datetime import datetime
from django.forms import ValidationError

def index(request):
    return render(request,'events/index.html')

def success(request):
    return render(request,'events/success.html')

def request_booking(request):
    ## Render booking form
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            fs = form.save(commit=False)
            ## Generate weekday from supplied date
            fs.weekday = fs.date.strftime("%A")
            fs.save()
            return success(request)

        else:
            print(form.errors)

    return render(request,'events/request_booking.html',{'form':form})