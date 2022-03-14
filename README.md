# BasisAT ( Basis Automation Tools ) - Backend

- Todo

  - Authentication API

    1. <s>/auth/login - generate and set JWT and save user information on MongoDB</s>
    2. <s>/auth/logout - Return only http status-code 202</s>
    3. <s>/auth/check - Check whether JWT is valid. Return User Information if valid. Otherwise, Abort 401 Error</s>

  - HomePage API
    1. <s>/home : GET - Get Homepage Description</s>
    2. <s>/home : PUT - Edit Homepage Description</s>

- UnitTest

  - Authentication

    1. /auth/login
    2. /auth/logout
    3. /auth/check

- OpenAPI Documentation

  - Authentication

    1. <s>/auth/login - POST</s>
    2. <s>/auth/logout - POST</s>
    3. <s>/auth/check - GET</s>

  - HomePage

    1. <s>/home - GET</s>
    2. <s>/home - PUT</s>
