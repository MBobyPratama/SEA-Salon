from django.contrib import admin
from .models import CustomUser, Reservation, Review, Service, Branch

admin.site.register(CustomUser)
admin.site.register(Reservation)
admin.site.register(Review)
admin.site.register(Service)
admin.site.register(Branch)