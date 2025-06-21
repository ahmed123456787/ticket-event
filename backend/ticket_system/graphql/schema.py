import graphene
from .query import Query
from .mutation import Mutation

# Define The Schema
schema = graphene.Schema(query=Query, mutation=Mutation)