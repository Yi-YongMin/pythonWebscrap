from flask import Flask
app=Flask("JobScrapper")
@app.route("/")
def home():
    return 'hey'
@app.route("/hello")
def hello():
    return 'hello you'
app.run("0.0.0.0")