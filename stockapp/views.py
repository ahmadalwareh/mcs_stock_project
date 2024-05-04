from django.shortcuts import render
from .forms import StockForm
import yfinance as yf

def stock_form(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            ticker_symbol = form.cleaned_data['ticker_symbol']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Fetch stock data from Yahoo Finance
            stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
            # Process the data and save it to the database (you need to implement this)

            return render(request, 'stockapp/stock_result.html', {'stock_data': stock_data})
    else:
        form = StockForm()
    return render(request, 'stockapp/stock_form.html', {'form': form})
