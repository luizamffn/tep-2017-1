from django.db import models
# from django.contrib.auth.models import User


# Create your models here.

class GameCategory(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Game(models.Model):
    created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=200, default='')
    release_date = models.DateField()
    game_category = models.ForeignKey(GameCategory, related_name='games', on_delete=models.CASCADE)
    played = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User',related_name='games',on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Player(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'),(FEMALE, 'Female'),)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=False)
    gender = models.CharField(max_length=2,
                              choices=GENDER_CHOICES,
                              default=MALE,
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Score(models.Model):
    score = models.IntegerField()
    score_date = models.DateField()
    player = models.ForeignKey(Player, related_name='scores', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-score',)