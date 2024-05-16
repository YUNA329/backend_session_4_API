from django.db import models

# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    agree = models.IntegerField(default=0)
    disagree = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    @property
    def agreeRate(self):
        total_votes = self.agree + self.disagree
        return self.agree / total_votes if total_votes !=0 else 0
    
    @property
    def disagreeRate(self):
        total_votes = self.agree + self.disagree
        return self.disagree / total_votes if total_votes !=0 else 0
    