from django.db import models
from hackathon.models import Hackathon
from django.contrib.auth.models import User





class Submission(models.Model):

    hackathon = models.ForeignKey( Hackathon, related_name='submission', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='submsission', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    summary = models.TextField()
    submission_files = models.FileField(upload_to='submissions/files/',blank=True,null=True)
    submission_links = models.URLField(blank=True,null=True)
    submission_images = models.ImageField(upload_to='submissions/images/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    






