from flask import Flask
import service

app = Flask(__name__)

@app.route("/")
def initial():
     print(service.values())
     return str(service.values())


if __name__ =='__main__':
    app.run(debug = True,port=5000,host="0.0.0.0")