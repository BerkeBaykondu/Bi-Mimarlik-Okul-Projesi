from django.db import models

# Create your models here.

class Projects(models.Model):
  STATUS = (
    ('True', 'Evet'),
    ('False', 'Hayır'),
  ) # açılan combobox tan gelecek. status combobox tan beslenecek

  image = models.ImageField(blank=True, upload_to='images/project')
  color = models.CharField(max_length=10, verbose_name='Color')
  project = models.CharField(max_length=100, verbose_name='Project')
  projectDescription = models.TextField(verbose_name='Project Description')
  city = models.CharField(max_length=100, verbose_name='City')
  status = models.CharField(max_length=10, choices = STATUS)
  create_at = models.DateTimeField(auto_now_add = True)
  update_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.project
