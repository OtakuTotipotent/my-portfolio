# pages/ app's views.py file
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm


class HomeView(TemplateView):
    template_name = "pages/home.html"


class ContactView(FormView):
    template_name = "pages/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        # send email
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]

        email_subject = f"Portfolio Contact Form: {name}"
        email_message = f"""
        Name: {name}
        Email: {email}
        
        Message:
        {message}
        """
        try:
            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],  # Send to yourself
                fail_silently=False,
            )
            messages.success(self.request, "Your message was sent successfully!")
        except Exception as e:
            messages.error(
                self.request, f"There was an error sending your message: {str(e)}"
            )

        return super().form_valid(form)


class OrdernowView(FormView):
    template_name = "pages/ordernow.html"
    form_class = ContactForm
    success_url = reverse_lazy("ordernow")

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]

        email_subject = f"Portfolio Order Form: {name}"
        email_message = f"""
        Name: {name}
        Email: {email}
        
        Message:
        {message}
        """
        try:
            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],  # Send to yourself
                fail_silently=False,
            )
            messages.success(
                self.request, "Your order request was submitted successfully!"
            )
        except Exception as e:
            messages.error(
                self.request, f"There was an error sending your message: {str(e)}"
            )
        return super().form_valid(form)
