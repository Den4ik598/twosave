from django.shortcuts import render
from .models import Food
import requests
import json
import os

def currency_data():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'currencies.json')
    with open(file_path, "r") as f:
        currency_data = json.loads(f.read())
    return currency_data


def index1(request):
    if request.method == "POST":

        # Get data from the html form
        amount = float(request.POST.get('amount'))
        currency_from = request.POST.get("currency_from")
        currency_to = request.POST.get("currency_to")
        radio = request.POST.get("oplata")
        # Get currency exchange rates
        url = f"https://open.er-api.com/v6/latest/{currency_from}"
        d = requests.get(url).json()

        # Converter
        if d["result"] == "success":
            # Get currency exchange of the target
            ex_target = d["rates"][currency_to]
            if radio == "sale":
                result = ex_target * amount * 100
                result1 = 0
            else:
                result0 = ex_target * amount * 1.01
                result = 0
            # Set 2 decimal places
            result = "{:.2f}".format(result)

            context = {
                "result": result,
                "currency_to": currency_to,
                "currency_data": currency_data(),
                "radio": radio
            }
            currency_save = Food(Name_Currency = currency_to, Curs_BANK = ex_target, Kurs_sell = 1, Kurs_buy= 1, number_of_currency= amount)
            currency_save.save()

            return render(request, "main/table.html", context)

    return render(request, "main/table.html", {"currency_data": currency_data()})


def report(request):
    return render(request,'main/report.html')
