from flask import Flask


# instance from Flask
app=Flask(__name__)




@app.route('/')
def home():
    return "welcome to flask"


# to run locally
if __name__=="__main__":
    app.run()

