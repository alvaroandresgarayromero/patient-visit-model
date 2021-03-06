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
export ADMIN_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxpOVB1aGNoTUNSa2NNUHN1YV9TMCJ9.eyJpc3MiOiJodHRwczovL2Rldi1hbWo5ZXh1YS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA5NTg0MTc1ZjIxNjgwMDZiNWMwOGE2IiwiYXVkIjpbIlBhdGllbnRWaXN0IiwiaHR0cHM6Ly9kZXYtYW1qOWV4dWEudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMjE3NTgwNiwiZXhwIjoxNjIyMjQ3NzkxLCJhenAiOiJLSU9YU3h6ZE9xem53elV6QktISjM1UWpFbFRkTjJvQSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6dmlzaXRzIiwiZGVsZXRlOnZpdGFsLXNpZ25zIiwicGF0Y2g6dmlzaXRzIiwicGF0Y2g6dml0YWwtc2lnbnMiLCJwb3N0OnZpc2l0cyIsInBvc3Q6dml0YWwtc2lnbnMiLCJyZWFkOnBhdGllbnQtZGF0YSJdfQ.wvXfZBbHfBx2_fraJfFtP2mv5Z5aYgaJkCu2x5H99RFAN9lbB00ZbsUyMu5HElk3hx3NqG4VQk2tff-4sKbjQaA4Y-F40pRICTM8KdC5rrtx8XB6X37o_0oO7rmAeJ6CCaY3JFFaqliA2iVml38lunGEfYuPpvHpnbqRtCKBNU1IrkwVrc3ADbZQkP0XLqGIbusDPkFdAaxBjWMWSlgbHXDphZKWfzKj_iWYj83KQkUJELrvVwkyGWE4FMzpY8fSlTmarz8-NjNPXfpGyzq7haAEYF7JMac4mJ-MEumqKy_jkkE03dvsZibUdlDUPp1wNukPv3pxlut1NTTCOo3XgQ"
export NURSE1_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxpOVB1aGNoTUNSa2NNUHN1YV9TMCJ9.eyJpc3MiOiJodHRwczovL2Rldi1hbWo5ZXh1YS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA5NTg0NDc5MjAxMzkwMDY4ZWNlNTM5IiwiYXVkIjpbIlBhdGllbnRWaXN0IiwiaHR0cHM6Ly9kZXYtYW1qOWV4dWEudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMjE3NTkxMiwiZXhwIjoxNjIyMjQ3ODk3LCJhenAiOiJLSU9YU3h6ZE9xem53elV6QktISjM1UWpFbFRkTjJvQSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJwYXRjaDp2aXNpdHMiLCJwYXRjaDp2aXRhbC1zaWducyIsInBvc3Q6dmlzaXRzIiwicG9zdDp2aXRhbC1zaWducyIsInJlYWQ6cGF0aWVudC1kYXRhIl19.AWmnyHcb81dY0uXZYL1ceuxAto68MgNN0sfuJmw3aCVjOwvSxG07EqQNCiyuf3pmX3Ac5Xywpv5-JeSKjsyEXRyte9sNun9zckIUXaLc1I_YoWutub_gsdC0yx97PaUT-pY4i-MGNsXxRbfEyNm8MKwz4wejOYL-cogR33mlF4DHB_dgJYPVHqYUm3RkUw58-yPJk4BLBXUPVclN8paIB50VuUYSBEec4NdKW6hiuh1Vn5iqreCOHKeTmssSkHlwe2DCyK82pHIv1zHw1HCdF9fwJDXkCube56IpMR5fzKj6HxXFz9llKlGkIJXRibHZ1CKb54CbkgEAn8lDi7IZEA"
export NURSE2_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxpOVB1aGNoTUNSa2NNUHN1YV9TMCJ9.eyJpc3MiOiJodHRwczovL2Rldi1hbWo5ZXh1YS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjBhZmNhYzk0MDJlYjAwMDY4NGVmMTk4IiwiYXVkIjpbIlBhdGllbnRWaXN0IiwiaHR0cHM6Ly9kZXYtYW1qOWV4dWEudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMjE3NTk4MSwiZXhwIjoxNjIyMjQ3OTY2LCJhenAiOiJLSU9YU3h6ZE9xem53elV6QktISjM1UWpFbFRkTjJvQSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJwYXRjaDp2aXNpdHMiLCJwYXRjaDp2aXRhbC1zaWducyIsInBvc3Q6dmlzaXRzIiwicG9zdDp2aXRhbC1zaWducyIsInJlYWQ6cGF0aWVudC1kYXRhIl19.RIupQiG9J5NYpmVsmmFJq41gjI6RbC4G8u94t8rmTy29g17zl3Bh4sC0_B-15R4iwZihHspE62C1Z3P9Ohu8Fqd9zcQ4ho4i5kNx5KQbO6N7vXL0tjNAYRvD_fw0XoD8TFQinE2xpIlaB22Tqcrb2xdtRS8eRnT9A4phCWUTIxuY1W6T0otIEF6VFWGZbu-OVXzjnxcaNrzZ4vHEae1nxIHcsn8ZHFEXHfRkMbS_zs3RiNujFUP-rZZVSe99XMyjtZKYkocZ_diQa1qvt9WdVrrx6eMArzpYw-YvoapA-2nzOokONqAoFOhRkrbki2hNGqeele0aV7R_iEdePWVkDw"
export PATIENT1_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxpOVB1aGNoTUNSa2NNUHN1YV9TMCJ9.eyJpc3MiOiJodHRwczovL2Rldi1hbWo5ZXh1YS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA5NTg0YjhhYmVhOGQwMDZhNGRkNDc4IiwiYXVkIjpbIlBhdGllbnRWaXN0IiwiaHR0cHM6Ly9kZXYtYW1qOWV4dWEudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMjE3NjA0NCwiZXhwIjoxNjIyMjQ4MDI5LCJhenAiOiJLSU9YU3h6ZE9xem53elV6QktISjM1UWpFbFRkTjJvQSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJyZWFkOnJlc3RyaWN0aXZlLXBhdGllbnQtZGF0YSJdfQ.fy0EO3ZXQSbqgGeIlzM7lZq49qx_RqdkOb7DorZJ4VvJGZBQHT1hhE8HR1w_Z5jmwxddpvpo2Fej-6aFzonpGyn4MceN0iXdNWAVSGN834jzd0xg7XNWRHN5Yc7BmBcoYxy1yQnDFIdrWkyIHbiM21WlyuSK5saPYwZeBOC7c7BfaeFeVcCjVowcL9V1Rj78uQBi0ZikcJtV1Z5RGIkkBHz4nxrUSmkFHcAb0Duq9Vrq-aPVe7MNsn4F_F_-z1FPF9W01u5k5f8dW9gioWsKPbKEN1HMvmKAGyS6EtdfbpnGBtwYCqfxi45yLl_ahHDz5lzsmILfWtcB83M3W46h6w"
export PATIENT2_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxpOVB1aGNoTUNSa2NNUHN1YV9TMCJ9.eyJpc3MiOiJodHRwczovL2Rldi1hbWo5ZXh1YS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA5NTg0ZTA1N2FmMjEwMDY5YTZlNGYxIiwiYXVkIjpbIlBhdGllbnRWaXN0IiwiaHR0cHM6Ly9kZXYtYW1qOWV4dWEudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMjE3NjEwNSwiZXhwIjoxNjIyMjQ4MDkwLCJhenAiOiJLSU9YU3h6ZE9xem53elV6QktISjM1UWpFbFRkTjJvQSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJyZWFkOnJlc3RyaWN0aXZlLXBhdGllbnQtZGF0YSJdfQ.CAu7lGDA38aDbIpga2WNukurAImTgLK_o7x07IIv_G--AF2EYeBbFDebus_n4jmWfmqIUKaZ1pAjH9bN9yrnVrADB6AItFhHAxa7m1NC3PfOEeys9BkabOL66LQba7JorBVmDngeZ2_nFxdmvM5kHD7BKM-GJbpXyfsp17TWHM7XqizPhTrEIDQIQNA_4Fv7dAGQygyFi9z56yTECtVjOVzIS43nxu0OYoyZru5n0z7UKsNy6dQPwsjjqCT4umlRGC3fFl-dU_oeTwQDb5pzs0_EUOLrauQWysDQ_5FzpwlUBurc66XDT-IbUGEglivg05_4aW76eQKG722DgrSnPg"

# USER CREDENTIALS (for reference)
ADMIN_EMAIL="admin@nursevisitmodel.com"
NURSE_1_EMAIL="nurse@nursevisitmodel.com"
NURSE_2_EMAIL="nurse_2@nursevisitmodel.com"
PATIENT_1_EMAIL="patient_nursepatientmodel_1@gmail.com"
PATIENT_2_EMAIL="patient_nursepatientmodel_2@gmail.com"

USERS_PASSWORD="Alvaro123"


