from django.db import models


class Player(models.Model):
    age = models.IntegerField()
    lastname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    tmt_id = models.IntegerField()

    def __str__(self):
        return f"{self.lastname}, {self.name}"

class PlayerInRanking(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    points = models.IntegerField()
    ranking = models.ForeignKey('Ranking', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ranking} - {self.player.lastname}, {self.player.name} - {self.points}"

class Ranking(models.Model):
    date = models.DateField()
    players = models.ManyToManyField(Player, through='PlayerInRanking')
    league = models.ForeignKey('League', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}"

class Tournament(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(Player, through='PlayerInTournament')

    def __str__(self):
        return f"{self.name} - {self.date}"

class PlayerInTournament(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.tournament} - {self.player.lastname}, {self.player.name} - {self.points}"

class League(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
