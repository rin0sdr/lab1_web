import requests
url = 'https://newton.vercel.app/api/v2/derive/x^2-2x'
response = requests.get(url)

# Result
data = response.json()
result = data['result']

print(result) # prints "2x-2"

#web page in Python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return result
if __name__ == "__main__":
    app.run()
