from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=18)
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    email = models.EmailField()
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('X', 'Not specified')
    )
    xp = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER)
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=18)
    tag = models.CharField(max_length=3)

class PlayerTeam(models.Model):
    player = models.ForeignKey(Player)
    team = models.ForeignKey(Team)

class Platform(models.Model):
    name = models.CharField(max_length=18)

class Game(models.Model):
    name = models.CharField(max_length=18)
    def __str__(self):
        return self.name

class PlatformGame(models.Model):
    game = models.ForeignKey(Game)
    platform = models.ForeignKey(Platform)

class Match(models.Model):
    start_time = models.DateTimeField()

class Ladder(models.Model):
    name = models.CharField(max_length=18)
    game = models.ForeignKey(Game)

class TeamMatch(models.Model):
    match = models.ForeignKey(Match)
    team = models.ForeignKey(Team)
    ladder = models.ForeignKey(Ladder)

class Level(models.Model):
    name = models.CharField(max_length=20)