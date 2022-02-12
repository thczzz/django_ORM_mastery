from django import forms
import decimal

from django.core.exceptions import ValidationError

from .models import customer


class Payment(forms.Form):
    payor = forms.CharField(max_length=30)
    payee = forms.CharField(max_length=30)
    amount = forms.CharField(max_length=30)

    def clean(self):
        cleaned_data = super().clean()
        sender_name = cleaned_data["payor"]
        sender = customer.objects.get(name=sender_name)
        funds_to_send = decimal.Decimal(cleaned_data["amount"])
        if funds_to_send > sender.balance:
            self.add_error('payor', "Insufficient funds.")
