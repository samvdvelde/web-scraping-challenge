from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


app = Flask(__name__)



# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_data")

@app.route("/")
def home():




    return render_template("index.html", data=data)



@app.route("/scrape")
def scrape():

    mars_data = scrape_mars.scrape()




    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)