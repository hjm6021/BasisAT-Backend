import requests
import config


def login(name, password):
    return requests.post(
        config.blasURL,
        data={"name": name, "password": password},
    )
