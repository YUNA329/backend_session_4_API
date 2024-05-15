from rest_framework import serializers
from polls.models import Poll

class PollSerializer(serializers.ModelSerializer):
    agree_rate = serializers.SerializerMethodField()
    disagree_rate = serializers.SerializerMethodField()
    
    class Meta:
        model = Poll
        fields = ['id','title', 'description', 'agree', 'disagree', 'agree_rate', 'disagree_rate', 'created_at']
    
    def get_agree_rate(self,obj):
        total_votes = obj.agree + obj.disagree
        return obj.agree / total_votes if total_votes != 0 else 0
    
    def get_disagree_rate(self,obj):
        total_votes = obj.agree + obj.disagree
        return obj.disagree / total_votes if total_votes != 0 else 0
        

class PollRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['title', 'description']