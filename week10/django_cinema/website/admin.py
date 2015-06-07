from django.contrib import admin
from .models import Movie, Projection, Rating, Reservation

admin.site.register(Movie)
admin.site.register(Projection)
admin.site.register(Rating)
admin.site.register(Reservation)
