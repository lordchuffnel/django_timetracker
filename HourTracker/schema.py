import graphene

import timecard.schema


class Query(timecard.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)