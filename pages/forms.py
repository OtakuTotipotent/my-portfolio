from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Please Enter Your Name"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Your Email Address Goes Here"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your Message", "rows": 5})
    )
