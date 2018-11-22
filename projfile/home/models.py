from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User
# Create your models here.
class crime_t(models.Model):

    date = models.DateTimeField(auto_now_add=True, db_index=True)
    address = models.CharField(max_length=50)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    description = models.CharField(db_index=True, max_length=100)
    location_desc = models.CharField(max_length=30, db_index=True)
    arrest = models.CharField(max_length=30, null=True)
    beat = models.IntegerField(null=True)
    updated_time = models.DateTimeField(null=True)
    violations = models.IntegerField(null=True)
    intersection = models.CharField(max_length=50, null=True)
    created_by_user = models.BooleanField(default=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        default=None
    )



class chat_vocab_t(models.Model):
    vocab = models.CharField(max_length=50, null=False)
    date = models.DateTimeField(auto_now_add=True)
    side = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=30, null=True)

class new_format(models.Model):
    id = models.IntegerField(primary_key=True)
    new_date = models.CharField(max_length = 7)
    description = models.CharField(max_length=100)
    new_count = models.BigIntegerField()
    class Meta:
        unique_together = (("new_date", "description"),)
class Meta:
    managed = False
    db_table = 'home_new_format'

class vocab_freq_central(models.Model):
    vocab = models.CharField(max_length=50, null=False)
    frequency = models.BigIntegerField(null=False)
 
class Meta:
    managed = False
    db_table = 'home_vocab_freq_central'

class vocab_freq_west(models.Model):
    vocab = models.CharField(max_length=50, null=False)
    frequency = models.BigIntegerField(null=False)
 
class Meta:
    managed = False
    db_table = 'home_vocab_freq_west'

class vocab_freq_east(models.Model):
    vocab = models.CharField(max_length=50, null=False)
    frequency = models.BigIntegerField(null=False)
 
class Meta:
    managed = False
    db_table = 'home_vocab_freq_east'

class vocab_freq_south(models.Model):
    vocab = models.CharField(max_length=50, null=False)
    frequency = models.BigIntegerField(null=False)
 
class Meta:
    managed = False
    db_table = 'home_vocab_freq_south'

class vocab_freq_north(models.Model):
    vocab = models.CharField(max_length=50, null=False)
    frequency = models.BigIntegerField(null=False)
 
class Meta:
    managed = False
    db_table = 'home_vocab_freq_north'

