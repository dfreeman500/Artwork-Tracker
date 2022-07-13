from flask import Flask
from flask_graphql import GraphQLView
from schemas import schema, ArtistDBModel, ArtworkDBModel
from db import session
import webbrowser


app = Flask(__name__)


# url rule that takes in graphQL endpoint
# only need one endpoint


app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True
    )
)





if __name__ == "__main__":
    webbrowser.open("http://localhost:5000/graphql")

app.run(debug=True,use_reloader=False)