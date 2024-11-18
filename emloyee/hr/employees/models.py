from django.db import models
class Employees(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.TextField(max_length=100)
    salary = models.FloatField()
