from django.core.management.base import BaseCommand
from core.factories import (
    HostFactory,
    ListingFactory,
    ListingPhotoFactory,
    ReviewFactory,
)


class Command(BaseCommand):
    help = "Generates sample data for the models"

    def handle(self, *args, **options):
        # Generate a batch of instances
        for _ in range(10):
            host = HostFactory()
            listing = ListingFactory(host=host)
            photos = [ListingPhotoFactory(listing=listing) for _ in range(3)]
            listing.photos.add(*photos)
            ReviewFactory(listing=listing)

        self.stdout.write(self.style.SUCCESS("Successfully generated sample data"))
