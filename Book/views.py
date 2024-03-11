from django.shortcuts import render, redirect
from .models import Sheets, Buyers, Order
from django.db.models import Q
from django.http import HttpResponseRedirect

# Create your views here.
def show(request):
    sheets = Sheets.objects.all()
    return render(request, 'Pavel_1.html', {'sheets': sheets})

def descrip(request, sheet_id):
    sheet = Sheets.objects.get(id=sheet_id)
    return render(request, '1.html', {'sheet': sheet, 'sheet_id': sheet_id})


def show_compositor(request, compositor):
    sheets = Sheets.objects.filter(Q(compositors__iexact=compositor) | Q(compositors__icontains=compositor))
    return render(request, 'compositor.html', {'sheets': sheets, 'compositor': compositor})

def search_sheets(request):
    query = request.GET.get('q', '')
    sheets = Sheets.objects.filter(Q(name__icontains=query) | Q(name__icontains=query.capitalize()))
    return render(request, 'search_sheets.html', {'sheets': sheets, 'query': query})

def show_genre(request, genre):
    sheets = Sheets.objects.filter(genre=genre)
    return render(request, 'show_genre.html', {'sheets': sheets, 'genre': genre})

def submit_order(request, sheet_id):  # sheet_id передается как аргумент
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST['fname']
        address = request.POST['address']
        delivery = request.POST['delivery']
        phone = request.POST['phone']
        telegram = request.POST['telegram']
        additional = request.POST['additional']

        # Получаем лист по id
        sheet = Sheets.objects.get(id=sheet_id)
        print(sheet)

        # Создаем нового покупателя и заказ
        buyer = Buyers.objects.create(name=name, sheets=sheet)  # Устанавливаем лист для покупателя
        order = Order.objects.create(buyer=buyer, sheet=sheet, address=address, delivery=delivery, phone=phone, telegram=telegram, additional=additional)

        # Перенаправляем пользователя на страницу благодарности (или любую другую страницу)
        return redirect('Pavel_1')

    # Если метод не POST (например, GET), мы просто отображаем форму
    return render(request, 'order_form.html', {'sheet_id': sheet_id})
