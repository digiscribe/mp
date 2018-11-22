from flask import Flask

# create app object
app = Flask(__name__)


# use decorator patter to link view function to url
@app.route("/")
@app.route("/hello")


#define the view using a function, which returns a string
def hello_world():
    return "Hello biatches!"

    
# start dev server using run() method
if __name__ == "__main__":
    app.run()

