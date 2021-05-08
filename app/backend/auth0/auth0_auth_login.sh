source setup.sh
echo "https://$AUTH0_DOMAIN/authorize?audience=$AUTH0_AUDIENCE&scope=$AUTH0_SCOPE&response_type=token&client_id=$AUTH0_CLIENT_ID&redirect_uri=$AUTH0_CALLBACK_URL"