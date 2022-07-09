from db import Artist, Artwork, Base, engine

print("Create The Database")

Base.metadata.create_all(bind=engine)

# run once
