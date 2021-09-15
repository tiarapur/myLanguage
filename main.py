#to run the website and to show the errors in the page

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
