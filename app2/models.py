from django.db import models

# Create your models here.

# class Person(models.Model):
#     name = models.CharField(max_length=200)
#     age = models.IntegerField()
#     mobile_num = models.IntegerField()
#     address = models.CharField(max_length=100)

#     class Meta:
#         db_table = "person"
#     def __str__(self):
#         return f"{self.name}.......{self.address}"


class student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    mobile_num = models.IntegerField()
    address = models.CharField(max_length=100)
    salary = models.IntegerField()

    class Meta:
        db_table = "student"
