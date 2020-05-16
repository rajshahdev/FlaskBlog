from flaskblog import app
#now the flaskblog is a folder(package) now when we working with this types of pakcages
# there is 1 important file called __init__ and when we call from flaskblog import app
# then it runs the __init__ file only.


if __name__ == '__main__':
    app.run(debug = True)