from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    create_engine,
    String,
    Integer,
    Column,
    ForeignKey,
    Text
)
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from connection import connection_string

Base = declarative_base()

engine = create_engine(connection_string, echo=True)

session = scoped_session(
    sessionmaker(bind=engine)
)

Base.query = session.query_property()

"""
table artist:
id - primary key
name : str
email: str
artist_img_url: str

table artwork:
id - primary key
title: str
year: int
artwork_img_url: str
artist_id -> artist.id
"""


class Artist(Base):
    __tablename__ = "artist"
    id = Column(Integer(), primary_key=True)
    name = Column(String(45), nullable=False)
    email = Column(String(80))
    artist_img_url = Column(Text())
    artwork = relationship("Artwork", backref="artist")

    def __repr__(self):
        return f"<Artist {self.name}>"


class Artwork(Base):
    __tablename__ = "artwork"
    id = Column(Integer(), primary_key=True)
    title = Column(String(80), nullable=False)
    year = Column(Integer())
    artwork_img_url = Column(Text())
    artwork_type = Column(String(80))
    artist_id = Column(Integer(), ForeignKey("artist.id"))

    def __repr__(self):
        return f"<Artwork {self.title}>"
