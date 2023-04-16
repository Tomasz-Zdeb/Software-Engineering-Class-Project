from api import app

if __name__ == '__main__':
    # When developing debug can be set to True to hot reload
    app.run(host="0.0.0.0", port=5000, debug=False)