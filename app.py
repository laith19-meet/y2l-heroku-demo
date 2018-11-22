from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_page():
    return "MY NAME IS BETER, BETER WITH B , B AS IN BEOBLE."

if __name__ == '__main__':
    app.run(debug=True)

