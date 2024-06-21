from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    tmt_id = models.IntegerField()

    def __str__(self):
        return f"{self.lastname}, {self.name}"
