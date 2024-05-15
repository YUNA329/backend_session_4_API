from django.db import models

# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    agree = models.IntegerField(default=0)
    disagree = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def agree_rate(self):
        total_votes = self.agree + self.disagree
        return self.agree / total_votes if total_votes !=0 else 0
    
    @property
    def disagree_rate(self):
        total_votes = self.agree + self.disagree
        return self.disagree / total_votes if total_votes !=0 else 0
    