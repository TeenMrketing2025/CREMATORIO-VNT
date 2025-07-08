import logging
import os
from flask import Flask, redirect


from app import create_app


app = create_app()

@app.route("/")
def home():
    return redirect("https://crematoriovirgendelanatividadtpp.com/")

if __name__ == "__main__":
    logging.info("Flask app started")
    port  =  int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
