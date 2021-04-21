from django.db import models


class Position(models.Model):
    designation = models.CharField(max_length=100)
    experience = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


availability_choices = (
    ("Full-Time Internship", "Full-Time Internship"),
    ("Part-Time Internship", "Part-Time Internship"),
    ("Open-Source Contribution", "Open-Source Contribution"),
)


class Job(models.Model):
    position = models.ForeignKey("main_app.Position", on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    college = models.CharField(max_length=100)
    graduation_year = models.CharField(max_length=100)
    resume = models.FileField(null=True, blank=True)
    skills = models.TextField()
    other_details = models.TextField(null=True, blank=True)
    github = models.CharField(max_length=256, null=True, blank=True)
    linkedin = models.CharField(max_length=256, null=True, blank=True)
    link = models.CharField(max_length=256, null=True, blank=True)
    expectations = models.TextField()
    availability = models.CharField(max_length=60, choices=availability_choices)
    datetime = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    hired = models.BooleanField(default=False)
    date_of_joining = models.DateField(blank=True, null=True)
    date_of_ending = models.DateField(blank=True, null=True)
