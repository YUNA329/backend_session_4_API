from rest_framework import serializers
from polls.models import Poll

class PollSerializer(serializers.ModelSerializer):
    agreeRate = serializers.SerializerMethodField()
    disagreeRate = serializers.SerializerMethodField()
    
    class Meta:
        model = Poll
        fields = ['id','title', 'description', 'agree', 'disagree', 'agreeRate', 'disagreeRate', 'createdAt']
    
    def get_agreeRate(self,obj):
        total_votes = obj.agree + obj.disagree
        return obj.agree / total_votes if total_votes != 0 else 0
    
    def get_disagreeRate(self,obj):
        total_votes = obj.agree + obj.disagree
        return obj.disagree / total_votes if total_votes != 0 else 0
        

class PollRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['title', 'description']