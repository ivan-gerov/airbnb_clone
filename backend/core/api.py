from typing import List
from django.shortcuts import get_object_or_404

from ninja import Router, Query

from .models import Listing
from .schema import ListingSchema, SearchParamsSchema, ListingResponseSchema

router = Router()


@router.get("/listings", response=List[ListingSchema])
def get_listings(request, search_params: Query[SearchParamsSchema]):
    filters = {}

    # Fix the search for dates and do an expansive search
    if search_params.location:
        filters["location__icontains"] = search_params.location

    if search_params.check_in_date:
        filters["start_date_availability__lte"] = search_params.check_in_date

    if search_params.check_out_date:
        filters["end_date_availability__gte"] = search_params.check_out_date

    if search_params.guests:
        filters["guests__gte"] = search_params.guests

    return Listing.objects.filter(**filters)


@router.get("/listings/{listing_id}", response=ListingResponseSchema)
def get_listing(request, listing_id: int):
    listing = get_object_or_404(Listing, id=listing_id)

    return {
        "listing": listing,
        "host": listing.host,
        "reviews": listing.reviews.all(),
    }
