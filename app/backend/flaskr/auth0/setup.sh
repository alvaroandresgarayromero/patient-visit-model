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
PATIENT_1_EMAIL="patient_nursepatientmodel_2@gmail.com"

USERS_PASSWORD="Alvaro123"

# To get to the AUTHO LOGINPAGE: $ source auth0LoginBrowser.sh


# TEMP DELETE
export USER_JWT_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxpOVB1aGNoTUNSa2NNUHN1YV9TMCJ9.eyJpc3MiOiJodHRwczovL2Rldi1hbWo5ZXh1YS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA5NTg0MTc1ZjIxNjgwMDZiNWMwOGE2IiwiYXVkIjpbIlBhdGllbnRWaXN0IiwiaHR0cHM6Ly9kZXYtYW1qOWV4dWEudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMTQ0ODA1NCwiZXhwIjoxNjIxNTIwMDM5LCJhenAiOiJLSU9YU3h6ZE9xem53elV6QktISjM1UWpFbFRkTjJvQSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6dmlzaXRzIiwiZGVsZXRlOnZpdGFsLXNpZ25zIiwicGF0Y2g6dmlzaXRzIiwicGF0Y2g6dml0YWwtc2lnbnMiLCJwb3N0OnZpc2l0cyIsInBvc3Q6dml0YWwtc2lnbnMiLCJyZWFkOnZpc2l0cyIsInJlYWQ6dml0YWwtc2lnbnMiXX0.BfVQVaZkf7PWLQDlA4V16Tz_r9lDMUIfoub_mxTfJM-wz4njKJ79-FoBB7mljLfbqEpE9WOpmkeI9xzc773IO4u8_rCpI3FBz53T2Cej8p2Hdy4UXk7BzFwrYAhjnVdm5VajXFfpt-zlE_dCR4znALrv_MvvtLy2-_HibBsFm4dlgEL-y6oonv9c6kCnYgLzexwHDau-SkP5fRvSr1e6jbrJkx8ly8D5vaSZHiYmclQSOJFNTT5QGruhXufImt5ywdputXQ-89gY9JfqwCRabNgGQWpJScHvT5f8wip0zYOJqeHlS3hAGKKMw35XdiWITJQS2DBJmTA2LfCrXmQ_WQ"
export BASE_URL="http://0.0.0.0:8080"

