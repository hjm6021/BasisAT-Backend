import requests
from flask import current_app


def login(name, password):
    return requests.post(
        current_app.config["BLAS_URL"],
        data={"name": name, "password": password},
    )
