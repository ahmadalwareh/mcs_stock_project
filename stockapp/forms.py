from django import forms

class StockForm(forms.Form):
    ticker_symbol = forms.CharField(label='Ticker Symbol', max_length=10)
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End Date')
