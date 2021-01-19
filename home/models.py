from django.db import models
# Create your models here.

class Settings(models.Model):
  logo = models.ImageField(blank=True, upload_to='images/')
  companyName = models.CharField(blank=True,max_length=100,verbose_name='Company Name')
  slogan = models.CharField(blank=True,max_length=100,verbose_name='Slogan')
  instagram = models.CharField(blank=True,max_length=255,verbose_name='Instagram')
  twitter = models.CharField(blank=True,max_length=255, verbose_name='Twitter')
  linkedin = models.CharField(blank=True,max_length=255, verbose_name='Linkedin')
  email = models.CharField(blank=True,max_length=150, verbose_name='Email')
  address = models.CharField(blank=True,max_length=150, verbose_name='Address')
  phone = models.CharField(blank=True,max_length=15, verbose_name='Phone')
  phone2 = models.CharField(blank=True,max_length=15, verbose_name='Phone 2')
  maps = models.CharField(blank=True,max_length=15, verbose_name='Map')
  def __str__(self):
    return self.companyName

class About(models.Model):
  STATUS = (
    ('True', 'Evet'),
    ('False', 'Hayır'),
  ) # açılan combobox tan gelecek. status combobox tan beslenecek
  icon = models.ImageField(blank=True, upload_to='uploads/')
  svg = models.TextField(blank=True, verbose_name='SVG')
  title = models.CharField(max_length=100, verbose_name='title')
  description = models.TextField(verbose_name='description')
  status = models.CharField(max_length=10, choices = STATUS)
  create_at = models.DateTimeField(auto_now_add = True)
  update_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.title