from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Vote(models.Model):
    title = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vote')
    description = models.TextField()
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    end_date = models.DateTimeField(auto_now_add=True)

class VoteOption(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='options')
    text = models.TextField()

class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='votes')
    option = models.ForeignKey(VoteOption, on_delete=models.CASCADE, related_name='options')
    voted_at = models.DateTimeField(auto_now_add=True)
