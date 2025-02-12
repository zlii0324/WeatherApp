from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = ""
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """ 获取城市天气数据 """
    params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "en"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "无法获取天气信息"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "请输入城市名称"}), 400
    
    data = get_weather(city)
    return jsonify(data)

if __name__ == "__main__":
    app.run()