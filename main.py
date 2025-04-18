from website import create_app

# Importing the create_app function from the website module
app = create_app()


if __name__ == '__main__':
    app.run(debug=True)