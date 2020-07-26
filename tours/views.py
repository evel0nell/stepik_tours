# Create your views here.
import random

from django.shortcuts import render

from django.views import View

import tours.tour_data as td

random_tours = dict(random.choices(list(td.tours.items()), k=6))


class MainView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(
            request, 'tours/main_tours.html', {"tours": random_tours}
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
