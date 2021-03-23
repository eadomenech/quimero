"""Run the app

python app.py
"""
from application import create_app

app = create_app('config.ProductionConfig')