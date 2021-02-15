import graphene

import ingredients.schema
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    verify_token = mutations.VerifyToken.Field()


class Query(ingredients.schema.Query,
            UserQuery,
            MeQuery,
            graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
