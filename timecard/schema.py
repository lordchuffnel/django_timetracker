import graphene

from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User
from .models import Timecard


class TimecardType(DjangoObjectType):
    class Meta:
        model = Timecard
        
class UserType(DjangoObjectType):
    class Meta: 
        model = User
        
        
class Query(object):
    user = graphene.Field(UserType, id=graphene.int(), username=graphene.String())
    
    all_timecards = graphene.List(TimecardType)
    
    timecard = graphene.Field(TimecardType, id=graphene.int(), username=graphene.String(), date=graphene.types.datetime.Date)
    
    def resolve_all_timecards(self, info, **kwargs):
        return Timecard.objects.all()
    
    def resolve_own_timecard(self, info, **kwargs):
        return Timecard.objects.select_related('User').all()
    
    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('username')
        
        if id is not None:
            return User.objects.get(pk=id)
        
        if name is not None:
            return User.objects.get(name=username)
        
        return None
    
    def resolve_timecard(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('username')
        date = kwargs.get('date')
        
        if id is not None:
            return Timecard.objects.get(pk=id)
        
        if name is not None:
            return Timecard.objects.get(name=username)
        
        if date is not None:
            return Timecard.objects.get(date=date)
        
        return None