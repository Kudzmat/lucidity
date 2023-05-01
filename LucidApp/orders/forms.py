from django import forms
from orders import models


class LocalForm(forms.ModelForm):
    class Meta:
        model = models.Local
        fields = ('date', 'amount', 'paid_from', 'tools_rate', 'sam_rate', 'notes')
        exclude = ['total_revenue', 'profit']  # fields excluded

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter the order amount'}),
            'tools_rate': forms.NumberInput(attrs={'placeholder': 'Enter rate for Tools'}),
            'sam_rate': forms.NumberInput(attrs={'placeholder': 'Enter rate from Samanco'}),
            'notes': forms.TextInput(attrs={'placeholder': 'Enter any notes'})
        }
        labels = {
            'date': 'Date of Order',
            'amount': 'Order Amount($)',
            'paid_from': 'Select Account Used',
            'tools_rate': 'Tools R Us Rate',
            'sam_rate': 'Samansco Rate',
            'notes': 'Order Notes'
        }
        choices = {
            'paid_from': "('', '--Select an account--'), (1, 'Samansco'), (2, 'Lucidity')"
        }
    """"
    # to show calender in html we would do this <input type="date">
    date = forms.DateField(
        label='Date of Order',
        widget=forms.TextInput(attrs={'type': 'date'}))

    amount = forms.IntegerField(required=True, label="Order Amount($)",
                                widget=forms.NumberInput(attrs={'placeholder': 'Enter the order amount'}))
    account = forms.ChoiceField(label='Select Account Used', choices=(
        ('', '--Select an account--'), (1, 'Samansco'), (2, 'Lucidity')))

    tools_rate = forms.IntegerField(required=True, label="Tools R Us Rate",
                                    widget=forms.NumberInput(attrs={'placeholder': 'Enter rate for Tools'}))
    sam_rate = forms.IntegerField(required=True, label="Samansco Rate",
                                  widget=forms.NumberInput(attrs={'placeholder': 'Enter rate from Samanco'}))
    """
