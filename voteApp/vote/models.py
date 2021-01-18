from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Candidates(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    post = models.CharField(max_length=255 , default = 'uncategorized')
    votes = models.ManyToManyField(User, related_name = 'casted_votes' )

    def number_of_votes(self):
        return self.votes.count()