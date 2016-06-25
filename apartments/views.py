from django.shortcuts import render_to_response
from apartments.models import Building, Apartment
from django.db.models import Min, Max


def apartments_list(request, building):
    b = Building.objects.filter(code=building)[0]
    apartments = Apartment.objects.filter(building__code=building).order_by('price')
    limits = apartments.aggregate(
        min_price=Min('price'),
        max_price=Max('price'),
        min_square=Min('square'),
        max_square=Max('square')
    )
    return render_to_response('apartments/apartments_list.html',
                              {
                                  'building': b,
                                  'apartments': apartments,
                                  'limits': limits
                              })


def apartment_detail(request, building, code):
    apartment = Apartment.objects.get(code=code)
    return render_to_response('apartments/apartment_detail.html', {'apartment': apartment})


def info(request):
    data = Building.objects.all()
    return render_to_response('apartments/info.html', {'data': data})
