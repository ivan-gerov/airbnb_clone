from django.contrib import admin

from .models import Host, Listing, ListingPhoto, Review

admin.site.register(Host)
admin.site.register(Listing)
admin.site.register(ListingPhoto)
admin.site.register(Review)
