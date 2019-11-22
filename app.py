from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import pandas as pd
from pandas import DataFrame


@app.route("/data")
def movielens():
    data = pd.read_csv("file:///C:/Users/user/Projects/MovieLens/ml-100k/u.item", sep="|")
    data = DataFrame(data, columns=['Movie_ID', 'Movie_Title'])
    return data.to_dict(orient='index')


@app.route("/pushdata", methods=['POST'])
def get_from_frontend():
    data = request.get_json('username')
    print(data)
    return data


if __name__ == "__main__":
    app.run()
