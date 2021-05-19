source setup.sh

echo "Copy the URL below into your browser.
Use incognito mode (ex: incognito chrome) to
login with multiple users since logout is not supported"
echo " "

echo "A JWT token will be generated"
echo "[optional] Update the user JWT environment variables
located in setup.sh if you'd like to
run curl examples as described in the README.md document"
echo " "

echo "https://$AUTH0_DOMAIN/authorize?audience=$AUTH0_AUDIENCE&scope=$AUTH0_SCOPE&response_type=token&client_id=$AUTH0_CLIENT_ID&redirect_uri=$AUTH0_CALLBACK_URL"