from typing import Optional, List
from datetime import date

from ninja import ModelSchema, Schema

from .models import Host, Listing, ListingPhoto, Review


class HostSchema(ModelSchema):
    total_reviews: int = 0
    class Meta:
        model = Host
        fields = "__all__"

    @staticmethod
    def resolve_total_reviews(obj):
        return obj.total_reviews()


class ListingSchema(ModelSchema):
    listing_photos: List[str] = []

    class Meta:
        model = Listing
        fields = "__all__"

    @staticmethod
    def resolve_listing_photos(obj):
        listing_photos = []
        if photos := obj.photos.all():
            for photo in photos:
                if photo.photo:
                    listing_photos.append(photo.photo.url)
        return listing_photos


class ReviewSchema(ModelSchema):
    class Meta:
        model = Review
        fields = "__all__"


class SearchParamsSchema(Schema):
    location: Optional[str] = None
    check_in_date: Optional[date] = None
    check_out_date: Optional[date] = None
    guests: Optional[int] = None


class ListingResponseSchema(Schema):
    listing: ListingSchema
    host: HostSchema
    reviews: List[ReviewSchema]
