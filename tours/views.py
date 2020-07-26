# Create your views here.
import random

from django.shortcuts import render

from django.views import View

from django.http import Http404

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
        if departure not in td.departures:
            raise Http404
        return render(

            request, 'tours/departure.html', {"departure": departure,
                                              "tours": td.tours,
                                              "from": td.departures[departure]}
        )


def handler404(request, exception=None):
    return render(request, "tours/404.html", status=404)


def handler500(request, exception=None):
    return render(request, "tours/500.html", status=500)


class TourView(View):

    def get(self, request, id=22):
        if id not in td.tours.keys():
            raise Http404
        return render(
            request, 'tours/tour.html', {"tours": td.tours[id]}
        )
