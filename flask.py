from modal import Image, App, wsgi_app

app = App("pixi-plot")  # Note: prior to April 2024, "app" was called "stub"
#image = Image.debian_slim().pip_install("flask")

image = Image.debian_slim().pip_install(
    "accelerate",
    "datasets",
    "gradio",
    "transformers",
    "torch",
    "torchvision",
    "torchaudio",
    "torchvideo",
    "wget",
    "Flask"
)

@app.function(image=image)
@wsgi_app()
def flask_app():
    from flask import Flask, request, render_template

    web_app = Flask(__name__)

    @web_app.get("/")
    def home():

        return render_template('index.html')

    @web_app.post("/echo")
    def echo():
        return request.json

    return web_app