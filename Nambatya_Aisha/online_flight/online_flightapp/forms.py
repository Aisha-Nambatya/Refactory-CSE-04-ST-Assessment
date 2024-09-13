from django import forms

class FlightBookingForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.Select(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    nationality = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    po_box = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    emergency_phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    passport_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    visa_document = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    departure_city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    destination_city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
