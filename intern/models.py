from django.db import models

class Intern(models.Model):
    emp_id= models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    clg_name = models.CharField(max_length=50)
    age= models.PositiveIntegerField()
    passing_year = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    finishing_date = models.DateField()

    def __str__(self):
        return self.name