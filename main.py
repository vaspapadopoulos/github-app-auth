import datetime
import os
import sys

import jwt

gh_app_id = os.getenv('GH_APP_ID')
gh_app_key = os.getenv('GH_APP_KEY')


if __name__ == "__main__":
    if not gh_app_id:
        sys.exit("GH_APP_ID is not set")
    if not gh_app_key:
        sys.exit("GH_APP_KEY is not set")

    with open(gh_app_key, "r") as key_file:
        key = key_file.read()

    now = int(datetime.datetime.now().timestamp())
    payload = {
        "iat": now - 60,
        "exp": now + 60 * 8,  # expire after 8 minutes
        "iss": gh_app_id
    }
    encoded = jwt.encode(payload=payload, key=key, algorithm="RS256")

    print(encoded)
