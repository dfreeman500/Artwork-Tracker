from db import Artist, Artwork, session

new_artist1 = Artist(
    name="Dana Johnson",
    email="dana@johnson.com",
    artist_img_url="https://images.unsplash.com/photo-1518518873111-6ca469aa4560"

)
new_artist2 = Artist(
    name="John Does",
    email="john@does.com",
    artist_img_url="https://images.unsplash.com/photo-1615208429553-d9982932ca5c"

)
new_artist3 = Artist(
    name="Jande Did",
    email="jane@did.com",
    artist_img_url="https://images.unsplash.com/photo-1535295972055-1c762f4483e5"

)

new_artwork1 = Artwork(
    title="The Bright Night",
    year=1990,
    artwork_img_url="https://images.unsplash.com/photo-1520209759809-a9bcb6cb3241",
    artwork_type="photo",
    artist=new_artist1
)

new_artwork2 = Artwork(
    title="Farewell to Aardvark",
    year=2000,
    artwork_img_url="https://images.unsplash.com/photo-1526900913101-88c16676ca02",
    artwork_type="photo",
    artist=new_artist2
)

new_artwork3 = Artwork(
    title="Copacetic",
    year=2010,
    artwork_img_url="https://images.unsplash.com/photo-1496458590512-56d2688442b1",
    artwork_type="photo",
    artist=new_artist3
)
session.add_all([new_artist1, new_artist2, new_artist3,
                new_artwork1, new_artwork2, new_artwork3])

session.commit()

#Queries
session.query(Artist).all()
session.query(Artwork).all()
session.query(Artwork.title).all()
