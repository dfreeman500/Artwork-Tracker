import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from db import (
    Artist as ArtistDBModel,
    Artwork as ArtworkDBModel,
    session
)


class ArtistSchema(SQLAlchemyObjectType):
    class Meta:
        model = ArtistDBModel
        interfaces = (relay.Node,)


class ArtworkSchema(SQLAlchemyObjectType):
    class Meta:
        model = ArtworkDBModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    all_artists = SQLAlchemyConnectionField(ArtistSchema.connection)

    all_artwork = SQLAlchemyConnectionField(ArtworkSchema.connection)


class ArtistMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=False)
        artist_img_url = graphene.String(required=False)

    artist = graphene.Field(lambda: ArtistSchema)

    def mutate(self, info, name, email, artist_img_url):
        artist = ArtistDBModel(
            name=name,
            email=email,
            artist_img_url=artist_img_url
        )

        session.add(artist)
        session.commit()

        return ArtistMutation(artist=artist)


class ArtworkMutation(graphene.Mutation):
    class Arguments:
        artist_id = graphene.Int()
        title = graphene.String(required=True)
        year = graphene.Int(required=False)
        artwork_img_url = graphene.String()  # string() vs Text
        artwork_type = graphene.String()

    artwork = graphene.Field(lambda: ArtworkSchema)

    def mutate(self, info, artist_id, title, year, artwork_img_url, artwork_type):
        artist = session.query(ArtistDBModel).filter_by(id=artist_id).firt()

        new_artwork = ArtworkDBModel(
            artist_id=artist_id,
            title=title,
            year=year,
            artwork_img_url=artwork_img_url,  # string() vs Text
            artwork_type=artwork_type)

        session.add(new_artwork)
        session.commit()

        return ArtworkMutation(artwork=new_artwork)


class Mutation(graphene.ObjectType):
    mutate_artist = ArtistMutation.Field()
    mutate_artwork = ArtworkMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
