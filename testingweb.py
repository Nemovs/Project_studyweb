import sys
print(sys.version_info)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Fuck the police!"
app.run(port='8000')
