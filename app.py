from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=["get", "post"])  # 127.0.0.1:5000/
def index():
    text = ""
    if request.method == "POST":
        area = request.form.get("area")
        # TODO: нормализация, стандартизация, ML-модели... 
        text = f"Стоимость квартиры площадью {area} кв. м. равна {float(area) * 100_000} рублей"
    return render_template("index.html", message=text)
