from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=["get", "post"])  # 127.0.0.1:5000/
def index():
    if request.method == "POST":
        area = request.form.get("area")
        print(area)
    return render_template("index.html")


if __name__ == "__main__":
    app.run()