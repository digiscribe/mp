from flask import Flask

# create app object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# use decorator patter to link view function to url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "Hello folks, so much easier!"


# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query


@app.route("/name/<name>")
def index(name):
    if name.lower() == 'avi':
        return "Hello, {}".format(name), 200
    else:
        return "Not Found", 404


# @app.route("/integer/<int:value>")
# def int_type(value):
#     print(value + 1)
#     return "int - correct"


# @app.route("/float/<float:value>")
# def float_type(value):
#     print(value + 1)
#     return "float - correct"

# @app.route("/path/<path:value>")
# def path_type(value):
#     print(value)
#     return "path - correct"




# start dev server using run() method
if __name__ == "__main__":
    app.run()

