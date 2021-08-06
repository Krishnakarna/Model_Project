from django.db import models

class EmployeeModel(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    salary = models.IntegerField()
    mail = models.EmailField(max_length=30)

    def __str__(self):
        return self.ename
