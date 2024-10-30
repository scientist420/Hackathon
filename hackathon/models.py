from django.db import models
from django.contrib.auth.models import User

class Hackathon(models.Model):

    Submission_Type_choice = [


        ('images','Images'),
        ('file', 'File'),
        ('link','Link')

]
    
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    background_image = models.ImageField(upload_to='hackathons/backgrounds/')
    hackathon_image = models.ImageField(upload_to='hackathons/images/')
    registered_users = models.ManyToManyField(User, related_name='registered_hackathons')
    Submission_Type = models.CharField(max_length=100, choices= Submission_Type_choice)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    reward_prize = models.CharField(max_length=150)
    created_by  = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title    
