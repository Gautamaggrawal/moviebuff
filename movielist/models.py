from django.db import models
from django.contrib.auth.models import User
# User should be able to add movies, along with a short review and rating of the movie if
# they have watched the movie.
#User should be able to create a bucket list of movies that they want to watch in future.


class Genre(models.Model):
    """
    Genre model : Table for movie Genres
    """
    name = models.CharField(max_length=500)
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
    def __str__(self):
        return self.name

class Movie(models.Model):
    """
    Movie model : model for Movies
    """
    name = models.CharField(max_length=500)
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    director = models.CharField(max_length=500)
    genre = models.ManyToManyField(Genre)
    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
    def __str__(self):
        return self.name



class UserMovieBucket(model.Model):
	moviename=models.Charfield(max_length=10)


class Usermovie(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="movieuser")
	watched=models.BooleanField()
	moviebucket=models.ForeignKey(UserMovieBucket,on_delete=models.CASCADE)
	moviename=models.Charfield(max_length=100)
	review=models.TextField()
	rating=models.FloatField()
	def __str__(self):
		return self.moviename

