from django import forms
from events.models import gig
import datetime

## Maximum open/close dates
year_open = datetime.date(2021,6,1)
year_close = datetime.date(2021,12,31)

class BookingForm(forms.ModelForm):
    date = forms.DateField(help_text="Enter your desired date: ")
    band = forms.CharField(max_length=32,help_text="Enter band name: ")
    weekday = forms.CharField(widget=forms.HiddenInput(),max_length=9,required=False)

    class Meta:
        model = gig
        fields = ('date','band')        

    def clean_date(self):
        data = self.cleaned_data.get('date')
        alternative = []
        ## Check booking isn't outside possible range
        if (data < year_open):
            raise forms.ValidationError("Earliest Booking: 2021-06-01")
        if (data > year_close):
            raise forms.ValidationError("Latest Booking: 2021-12-31")

        ## Wednesday Error
        if (data.strftime("%A") == "Wednesday"):
            alternative.append("We are closed on Wednesdays")
        
        ## Find alternative date
        if gig.objects.filter(date=data).exists():
            alternative.append("Booking Conflict! Alternative Dates: ")
            past,future = data,data
            
            ## If the date is a Wednesday, skip 2 days
            try:
                past -= datetime.timedelta(days=1)
                if past.strftime("%A") == "Wednesday":
                    past -= datetime.timedelta(days=1)
                gig.objects.get(date=past)
            except gig.DoesNotExist:
                alternative.append(past)

            try:
                future += datetime.timedelta(days=1)
                if future.strftime("%A") == "Wednesday":
                    future += datetime.timedelta(days=1)
                gig.objects.get(date=future)
            except gig.DoesNotExist:
                alternative.append(future)
            ## Report final alternative
            raise forms.ValidationError(alternative)
        return data

    
