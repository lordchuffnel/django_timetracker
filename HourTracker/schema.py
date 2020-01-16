import graphene

import timecard.schema


class Query(timecard.schema.Query, graphene.ObjectType):
    pass

class Mutation(timecard.schema.Mutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
