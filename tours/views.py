# Create your views here.
from django.shortcuts import render
from django.views import View

import tours.tour_data as td




class MainView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(
            request, 'tours/main_tours.html', {"tours": td.tours}
        )


class DepartureView(View):
    @staticmethod
    def get(request, departure="msk"):
        return render(

            request, 'tours/departure.html', {"departure": departure,
                                              "tours": td.tours,
                                              "from": td.departures[departure]}
        )


class TourView(View):
    def get(self, request, id=22):
        return render(
            request, 'tours/tour.html', {"tours": td.tours[id]}
        )
