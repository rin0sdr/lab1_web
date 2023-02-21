import requests
url = 'https://newton.vercel.app/api/v2/derive/x^2-2x'
response = requests.get(url)
data = response.json()
result = data['result']
print(result)
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return result
if __name__ == "__main__":
    app.run()
