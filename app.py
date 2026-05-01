from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Devops Succesful</h1>" \
    "<p> this include python+docker+git+AWS</p>"

if __main__==__name__ :
    app.run(host='0.0.0.0',port=5000)
