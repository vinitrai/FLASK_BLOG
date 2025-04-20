# this file is the program's main entry point
# import the app from the package-flaskblog
from flaskblog import create_app
app = create_app()
# run the app
if __name__ == '__main__':
    app.run(debug=True)