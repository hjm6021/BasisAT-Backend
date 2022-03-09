# BLAS API Configuration
BLAS_URL = "https://www.basis-service.com/blas777/api/v1/auth/login/"

# MongoDB Connection Configuration
MONGODB = "basisAT"
MONGODB_HOST = "localhost"
MONGODB_PORT = 27017

# JSON Web Tokens Configuration
JWT_SECRET_KEY = "jwtSecretKey"
JWT_ALGORITHM = "HS256"

# Create an APISpec
FLASGGER_TEMPLATE = {
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

FLASGGER_SETTING = {
    "title": "BasisAT API",
    "uiversion": 3,
    "specs_route": "/docs/",
}
