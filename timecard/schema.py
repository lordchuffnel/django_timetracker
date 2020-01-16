import graphene

from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User
from .models import Timecard


class TimecardType(DjangoObjectType):
    class Meta:
        model = Timecard
        
class CreateTimecard(graphene.Mutation):
    timecard = graphene.Field(lambda: TimecardType)
    
    class Arguments:
        id = graphene.ID()
        username = graphene.String(required=True)
        date = graphene.Date(required=True)
        start_time = graphene.DateTime(required=True)
        lunch = graphene.Boolean()
        end_time = graphene.DateTime(required=True)
        int_hours = graphene.Decimal()
        ext_hours = graphene.Decimal()
        
    def mutate(self, info, username, date, start_time, lunch, end_time, int_hours, ext_hours, id):
        timecard = Timecard(pk=id, username=username, 
                            date=date, 
                            start_time=start_time, 
                            lunch=lunch, 
                            end_time=end_time, 
                            int_hours=int_hours, 
                            ext_hours=ext_hours)
        return CreateTimecard(timecard = timecard)
    
class UpdateTimecard(graphene.Mutation):
    timecard = graphene.Field(lambda: TimecardType)
    
    class Arguments:
        id = graphene.String()
        updated_at = graphene.DateTime()
        
    def mutate(self, info, id, updated_at):
        timecard = Timecard.objects.get(pk=id)
        timecard.updated_at = updated_at
        timecard.save()
        return UpdateTimecard(timecard=timecard)
    
    
class UserType(DjangoObjectType):
    class Meta: 
        model = User
        
        
class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    
    all_timecards = graphene.List(TimecardType)
    
    timecard = graphene.Field(TimecardType, username=graphene.String(), date=graphene.Date())
    
    def resolve_all_timecards(self, info, **kwargs):
        return Timecard.objects.all()
    
    def resolve_own_timecard(self, info, **kwargs):
        return Timecard.objects.select_related('User').all()
    
    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()
    
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
    
class Mutations(graphene.ObjectType):
    create_timecard = CreateTimecard.Field()
    update_timecard = UpdateTimecard.Field()