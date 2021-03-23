import json
from flask import current_app
import os
import requests


def generate_request(url, params={}):
    url = current_app.config['API_URL'] + url
    response = requests.get(url, params=params, verify=False)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)

    return response.json()


def generate_request_json_post(url, params={}):
    url = current_app.config['API_URL'] + url
    response = requests.post(url, json=params)
    return response


def get_users(params={}):
    response = generate_request('users', params)
    if response:
        return response
    return None


def login_service(params={}):
    response = generate_request_json_post('auth/login', params)
    return response


def register_service(params={}):
    response = generate_request_json_post('auth/register', params)
    return response
