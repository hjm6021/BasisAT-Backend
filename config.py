# BLAS API Configuration
blasURL = "https://www.basis-service.com/blas777/api/v1/auth/login/"

# MongoDB Connection Configuration
mongoDb = "basisAT"
mongoHost = "localhost"
mongoPort = 27017

# JSON Web Tokens Configuration
jwtSecretKey = "jwtSecretKey"
jwtAlgorithm = "HS256"

# Create an APISpec
flasgger_template = {
    "swagger": "2.0",
    "info": {
        "title": "BasisAT RestAPI Documentation",
        "description": "This documentation is for BasisAT API",
        "version": "0.1.1",
        "contact": {
            "name": " : Jeongmin Han / System Development Team / Basis Corp.",
            "email": "jmhan@cyber-co.com",
        },
    },
}

flasgger_setting = {
    "title": "BasisAT API",
    "uiversion": 3,
    "specs_route": "/docs/",
}
