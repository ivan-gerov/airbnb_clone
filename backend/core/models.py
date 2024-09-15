from django.db import models


class Host(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="photos/%Y/%m/%d/")
    response_time = models.CharField(max_length=100)
    response_rate = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def total_reviews(self):
        reviews = []
        for listing in self.listings.all():
            reviews.extend(listing.reviews.all())
        return len(reviews)

class Listing(models.Model):
    title = models.CharField(max_length=100)
    list_date = models.DateTimeField(auto_now_add=True)
    start_date_availability = models.DateTimeField()
    end_date_availability = models.DateTimeField()
    stars = models.FloatField(default=0.0)
    short_description = models.CharField(max_length=200)
    long_description = models.TextField(max_length=500)
    location = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    is_published = models.BooleanField(default=True)
    host = models.ForeignKey(Host, on_delete=models.CASCADE, related_name="listings")
    guests = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class ListingPhoto(models.Model):
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.listing.title + " Photo" + str(self.id)


class Review(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="reviews"
    )
    name = models.CharField(max_length=100)
    stars = models.FloatField(default=0.0)
    review = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
