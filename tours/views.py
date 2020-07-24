# Create your views here.
from django.shortcuts import render
from django.views import View

class TestView(View):
    def get(self, request, *args,**kwargs):
        return render(request, '', {})
class MainView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(
            request, 'tours/main_tours.html'
        )


class DepartureView(View):
    @staticmethod
    def get(request, departure="msk"):
        return render(

            request, 'tours/departure.html'
        )


class TourView(View):
    def get(self, request, id=22):
        return render(
            request, 'tours/tour.html'
        )
