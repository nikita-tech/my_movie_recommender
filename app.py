from flask import Flask, jsonify
import pandas as pd


app = Flask(__name__)

@app.route("/data")
def movielens():
    data = pd.read_csv("file:///C:/Users/user/Projects/MovieLens/ml-100k/u.item" , sep="|")
    data = data.filter(["Movie_ID", "Movie_Title"])
    return data.to_json(orient='values')



if __name__ == "__main__":
    app.run()