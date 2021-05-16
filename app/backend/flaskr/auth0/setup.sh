#!/bin/bash

# this file is not used by the application other than the script run_setup.sh
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

# To get to the AUTHO LOGINPAGE: $ source run_setup.sh


# TEMP DELETE
export USER_JWT_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxpOVB1aGNoTUNSa2NNUHN1YV9TMCJ9.eyJpc3MiOiJodHRwczovL2Rldi1hbWo5ZXh1YS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA5NTg0MTc1ZjIxNjgwMDZiNWMwOGE2IiwiYXVkIjpbIlBhdGllbnRWaXN0IiwiaHR0cHM6Ly9kZXYtYW1qOWV4dWEudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMDkxMzYwMywiZXhwIjoxNjIxMDAwMDAzLCJhenAiOiJwRWdwaWZwQkJQRHdvWkNPNVZYaHRzaE4wZjBHVWlNYiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJndHkiOiJwYXNzd29yZCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTp2aXNpdHMiLCJkZWxldGU6dml0YWwtc2lnbnMiLCJwYXRjaDp2aXNpdHMiLCJwYXRjaDp2aXRhbC1zaWducyIsInBvc3Q6dmlzaXRzIiwicG9zdDp2aXRhbC1zaWducyIsInJlYWQ6dmlzaXRzIiwicmVhZDp2aXRhbC1zaWducyJdfQ.ZOpRV7jURNO88jtHOhIx7MNflGObEjKznnzY27oRqtKbaWYBYm0Q3_ChBUF2P7vUwBo0FV8OMg8CYalUhkqG7m18_HalonDRbNiQEnBH0oL4HtnJ9WVx9L7dmtsy5yeoYHL_quARf3wlIMq8JAL3wpLldyg4xOw6xyAkBosD3fF6eIwZXsPJQ75nTSde1X3kXCKiIObLtGYZit94Aabo0F31t6PFir9RLzseuqb8xvjoBUt3CMHhcZu1fSzcO3or-QYf1kdtVpZB-jqST4EjSeVVhERXM6CC1qWeRrpUmXrv3MpbDP5VFm-YS9GzyZb0BJM9XjPkFyg05CSuEGKROA"
export BASE_URL="http://0.0.0.0:8080"

