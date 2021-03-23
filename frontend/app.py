"""Run the app locally

python app.py
"""
from application import create_app

if __name__ == '__main__':
    app = create_app('config.ProductionConfig')
    app.run(host='0.0.0.0', port='8000')
