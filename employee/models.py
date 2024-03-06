from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmployeeDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empcode = models.CharField(max_length=50)
    empdept = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=50, null=True)
    joiningdate = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

class EmployeeEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    course_pg = models.CharField(max_length=100, null=True)
    schoolcollege_pg = models.CharField(max_length=100, null=True)
    year_of_passing_pg = models.CharField(max_length=20, null=True)
    percentage_pg = models.CharField(max_length=30, null=True)

    course_grad = models.CharField(max_length=100, null=True)
    schoolcollege_grad = models.CharField(max_length=100, null=True)
    year_of_passing_grad = models.CharField(max_length=20, null=True)
    percentage_grad = models.CharField(max_length=30, null=True)

    course_hsec = models.CharField(max_length=100, null=True)
    schoolcollege_hsec = models.CharField(max_length=100, null=True)
    year_of_passing_hsec = models.CharField(max_length=20, null=True)
    percentage_hsec = models.CharField(max_length=30, null=True)

    course_sec = models.CharField(max_length=100, null=True)
    schoolcollege_sec = models.CharField(max_length=100, null=True)
    year_of_passing_sec = models.CharField(max_length=20, null=True)
    percentage_sec = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user.username
    
class EmployeeExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    company1name = models.CharField(max_length=100, null=True)
    company1designation = models.CharField(max_length=100, null=True)
    company1salary = models.CharField(max_length=100, null=True)
    company1duration = models.CharField(max_length=100, null=True)

    company2name = models.CharField(max_length=100, null=True)
    company2designation = models.CharField(max_length=100, null=True)
    company2salary = models.CharField(max_length=100, null=True)
    company2duration = models.CharField(max_length=100, null=True)

    company3name = models.CharField(max_length=100, null=True)
    company3designation = models.CharField(max_length=100, null=True)
    company3salary = models.CharField(max_length=100, null=True)
    company3duration = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username
    

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.submission_date}"

    
