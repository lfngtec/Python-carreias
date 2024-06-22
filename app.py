from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p>Hello, World teste Brasil!</p>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)