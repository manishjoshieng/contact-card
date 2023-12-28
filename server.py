from flask import Flask, render_template
import os

app = Flask(__name__)

IPADD  = os.environ.get("LOCAL_IP")
PORT   = os.environ.get("LOCAL_PORT")

@app.route("/manish-joshi")
def home():
    param = {
        "name" : "Manish Joshi",
        "position" : "Senior Software engineer",
        "media" : {
            "twitter" : "https://www.twitter.com/34joshi",
            "linkedin" : "https://www.linkedin.com/in/joshi-manish/",
            "topmate"   :   "https://topmate.io/manish_joshi93"
        }
    }
    return render_template('index.html',name = param["name"], position=param["position"], media=param["media"])




if __name__ == '__main__':
    print(f'Server running at {IPADD}:{PORT}')
    app.run(host=IPADD, port=PORT, debug=True)