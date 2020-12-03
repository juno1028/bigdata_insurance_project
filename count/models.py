from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Apply(models.Model):
    gender = models.CharField(max_length=200)
    age = models.IntegerField()
    height = models.FloatField()

    weight = models.FloatField()
    waist = models.FloatField()

    bp_judge = models.CharField(max_length=200)
    pulse_count_judge = models.CharField(max_length=200)

    bp_gluc = models.FloatField()
    bt_chol = models.FloatField()

    bt_trig = models.FloatField()
    bt_hb = models.FloatField()

    bt_crea = models.FloatField()
    bt_sgot = models.FloatField()

    bt_sgpt = models.FloatField()
    bt_rgpt = models.FloatField()

    bt_hbsa = models.CharField(max_length=200)

    smoke_flag = models.CharField(max_length=200)
    drinking_flag = models.CharField(max_length=200)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.created_date)