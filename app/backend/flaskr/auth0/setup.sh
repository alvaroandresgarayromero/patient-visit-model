#!/bin/bash

# this file is not used by the application other than the script auth0LoginBrowser.sh
# this file is part of the rubric requirements for udacity reviewers

# BASE URL
export BASE_URL="https://patient-visit-model.herokuapp.com"

# AUTHO CONFIG PARAMS: PatientVisit - REGULAR WEB APPLICATION
export AUTH0_DOMAIN="dev-amj9exua.us.auth0.com"
export AUTH0_SCOPE="openid profile email"
export ALGORITHMS="RSA256"
export AUTH0_AUDIENCE="PatientVist"
export AUTH0_CALLBACK_URL=""$BASE_URL"/login-results"
export AUTH0_CLIENT_ID="KIOXSxzdOqznwzUzBKHJ35QjElTdN2oA"
export AUTH0_CLIENT_SECRET="xtY_8QwJq8zdTLy6Sb27QSNRpTc8L90LJ6VYXu5quE5atN8t5m6Cg0u9P_U6hKRw"

# AUTHO CONFIG PARAMS: Management APIv2 MACHINE-TO-MACHINE APPLICATION
# To interact with the AUTH0 Management API v2 endpoints, we need to authenticate with an
# access token called the AUTH0 Management API token
export AUTH0_MANAGEMENT_AUDIENCE="https://dev-amj9exua.us.auth0.com/api/v2/"
export AUTH0_MANAGEMENT_CLIENT_ID="1yWQNQvCAvxA5vP0ndaQc3AkCtP7zf5f"
export AUTH0_MANAGEMENT_CLIENT_SECRET="RwnXauUXbRA8-WhBCbkxNZEC7XJwIA6EpIyiwz08n-HskBRedzxPlu1P4bhW_rj8"

# TOKENs were generated right before submitting the project for grading
export ADMIN_TOKEN="NONE"
export NURSE_TOKEN="NONE"
export PATIENT1_TOKEN="NONE"
export PATIENT2_TOKEN="NONE"

# USER CREDENTIALS (for reference)
ADMIN_EMAIL="admin@nursevisitmodel.com"
NURSE_EMAIL="nurse@nursevisitmodel.com"
PATIENT_1_EMAIL="patient_nursepatientmodel_1@gmail.com"
PATIENT_2_EMAIL="patient_nursepatientmodel_2@gmail.com"

USERS_PASSWORD="Alvaro123"

# To get to the AUTHO LOGINPAGE: $ source auth0LoginBrowser.sh


# TEMP DELETE
export USER_JWT_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxpOVB1aGNoTUNSa2NNUHN1YV9TMCJ9.eyJpc3MiOiJodHRwczovL2Rldi1hbWo5ZXh1YS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA5NTg0MTc1ZjIxNjgwMDZiNWMwOGE2IiwiYXVkIjpbIlBhdGllbnRWaXN0IiwiaHR0cHM6Ly9kZXYtYW1qOWV4dWEudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMjE0MTAwOCwiZXhwIjoxNjIyMjEyOTkzLCJhenAiOiJLSU9YU3h6ZE9xem53elV6QktISjM1UWpFbFRkTjJvQSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6dmlzaXRzIiwiZGVsZXRlOnZpdGFsLXNpZ25zIiwicGF0Y2g6dmlzaXRzIiwicGF0Y2g6dml0YWwtc2lnbnMiLCJwb3N0OnZpc2l0cyIsInBvc3Q6dml0YWwtc2lnbnMiLCJyZWFkOnBhdGllbnQtZGF0YSJdfQ.Z7x0MebHwMvXsMzAQcuE0y_5G0yH6ag1qQg6J0rJ_syy15C5t-WXCaTkV7yaeWiF5RntcS1PkPpbwEuFxu9lDXXsl8Lu4ZJufjhqX8x9YfrUD9EEarjDN6k0IswoOXhMNPNBB0WyaDN_ap4wE1iq_D4dq9zk9OSGagrYEegDQ5JKjXzszFBPIy9G8YAX9nEW6_OjFUPmsAnlKsLpBHqez0VSOO-yfnpL4D6Kgt36dGFKg3TxuJdXfovP5gjNSjyZ7QRfOOJNoX8XoE6rRAFb6wfNODnPQGLC_-c3mDa6IxfRR2fActHCIj8_D0X7OOfdAmQ7cLE9ABR8OsFQWtlrkg"
export BASE_URL="http://0.0.0.0:8080"

