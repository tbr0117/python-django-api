from django.db import models
from tastypie.resources import ModelResource
# from django.tastypie.resources import ModelResource

# Create your models here.
class Movie(models.Model):
    MovieName: models.CharField(max_length=175)
    MovieSubtitle: models.CharField(max_length=100)
    Genre: models.CharField(max_length=30)
    ReleaseDate: models.DateField()


class MovieResource(ModelResource):
    class Meta():
        queryset = Movie.objects.all()
        resource_name = "Movies"

