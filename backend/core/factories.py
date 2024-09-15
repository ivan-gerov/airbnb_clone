import os
from datetime import date, timedelta
import random
import shutil

import factory
from faker import Faker
from django.conf import settings
from django.core.files import File

from .models import Host, Listing, ListingPhoto, Review

fake = Faker()


class HostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Host

    name = factory.Faker("name")
    email = factory.Faker("email")
    phone = factory.Faker("phone_number")
    profile_picture = factory.django.ImageField()
    response_time = factory.Faker(
        "random_element", elements=("1 hour", "2 hours", "3 hours")
    )
    response_rate = factory.Faker("random_element", elements=("100%", "90%", "80%"))


class ListingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Listing

    stars = factory.Faker(
        "pydecimal",
        left_digits=1,
        right_digits=1,
        positive=True,
        min_value=1,
        max_value=5,
    )

    start_date_availability = factory.Faker(
        "date_between_dates", date_start=date(2024, 6, 1), date_end=date(2024, 8, 31)
    )
    end_date_availability = factory.LazyAttribute(
        lambda obj: obj.start_date_availability
        + timedelta(weeks=fake.random_int(min=1, max=2))
    )

    short_description = factory.Faker("sentence", nb_words=10)
    long_description = factory.Faker("text")

    location = factory.LazyAttribute(lambda _: f"{fake.city()}, {fake.country()}")

    price = factory.Faker("pyfloat", left_digits=5, right_digits=2, positive=True)
    is_published = factory.Faker("boolean")
    host = factory.SubFactory(HostFactory)
    guests = factory.Faker("random_int", min=1, max=10)

    @factory.post_generation
    def photos(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for photo in extracted:
                self.photos.add(photo)

    @staticmethod
    def generate_title():
        adjectives = ["Beautiful", "Cozy", "Modern", "Spacious", "Luxurious"]
        nouns = ["Villa", "Apartment", "House", "Condo", "Loft"]
        locations = [
            "in Downtown",
            "in the Beach",
            "with Ocean View",
            "with Mountain View",
            "near the Park",
        ]

        title = f"{random.choice(adjectives)} {random.choice(nouns)} {random.choice(locations)}"
        return title

    title = factory.LazyFunction(generate_title)


class ListingPhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ListingPhoto

    listing = factory.SubFactory(ListingFactory)
    name = factory.Faker("name")

    @factory.lazy_attribute
    def photo(self):
        image_dir = settings.PROJECT_DIR / "sample_images"
        image_name = random.choice(os.listdir(image_dir))
        image_path = os.path.join(image_dir, image_name)

        upload_dir = "photos"
        upload_path = os.path.join(upload_dir, image_name)
        shutil.copyfile(image_path, upload_path)

        # Open the copied file and save it
        return File(open(upload_path, "rb"))


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    listing = factory.SubFactory(ListingFactory)
    name = factory.Faker("name")
    stars = factory.Faker(
        "pydecimal",
        left_digits=1,
        right_digits=1,
        positive=True,
        min_value=1,
        max_value=5,
    )
    review = factory.Faker("text")
