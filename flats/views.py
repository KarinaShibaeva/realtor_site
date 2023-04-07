from django.shortcuts import render
from flats.models import Flat

def flat_list_view(request):
    flats=Flat.objects.all()
    context={"flats_list": flats}
    return render(request, "flats/flats_list.html",context)
