from django.shortcuts import render
from .models import Food
from .models import Number
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import requests
import datetime
import json
import os
import xlwt


def currency_data():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'currencies.json')
    with open(file_path, "r") as f:
        currency_data = json.loads(f.read())
    return currency_data


def ex(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename = Expenses' + \
                                      str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Expenses')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns= ['Name_Currency', 'ex_target', 'Curs_BANK', 'Kurs_buy',
                                 'number_of_currency', 'Date']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style = xlwt.XFStyle()

    rows = Food.objects.all().values_list('Name_Currency', 'Curs_BANK', 'Kurs_sell', 'Kurs_buy',
                                 'number_of_currency', 'Date')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)

    return response
def function(request):
    object = Food.objects.all()
    object.delete()
    return render(request,"main/report.html")
def Data_people(request):
    People = Number.objects.all()
    print(People)
    return render(request, "main/database.html", {'People': People})


def add_People(request):
    if request.method == "POST":
        username = request.POST.get('username')
        number =  request.POST.get('number')
        id = request.POST.get('id')
        phone = request.POST.get('phone')
        Inn = request.POST.get('Inn')
        people_save= Number(id = id , username = username , number = number, phone= phone , Inn = Inn)
        people_save.save()
        return HttpResponseRedirect('database/')
    else:
        return render(request, 'main/add.html')


def index1(request):
    if request.method == "POST":
        error = ''
        # Get data from the html form
        amount = float(request.POST.get('amount'))
        currency_from = request.POST.get("currency_from")
        currency_to = request.POST.get("currency_to")
        radio = request.POST.get("oplata")
        # Get currency exchange rates
        url = f"https://open.er-api.com/v6/latest/{currency_from}"
        d = requests.get(url).json()
        Date = datetime.datetime.today().replace(microsecond=0,second=0)
        # Converter
        if d["result"] == "success":
            # Get currency exchange of the target
            ex_target = d["rates"][currency_to]
            if radio == "sale":
                result = ex_target * amount * 1.03

            else:
                result = ex_target * amount * 1.01

            # Set 2 decimal places
            result = "{:.2f}".format(result)
            a = ex_target * amount * 1.03
            b = ex_target * amount * 1.01
            context = {
                "result": result,
                "currency_to": currency_to,
                "currency_data": currency_data(),
                "radio": radio

            }
            currency_save = Food(Name_Currency=currency_to, Curs_BANK=ex_target, Kurs_sell=a, Kurs_buy=b,
                                 number_of_currency=amount, Date= Date)
            currency_save.save()

            return render(request, "main/table.html", context)

    return render(request, "main/table.html", {"currency_data": currency_data()})


def report(request):
    Food_data = Food.objects.all()
    return render(request, 'main/report.html', {'Food': Food_data})


