# github-app-auth

A simple Python script to authenticate to GitHub as a GitHub App.

The script is based on the Ruby script found in
[Authenticating as a GitHub App](https://docs.github.com/en/developers/apps/building-github-apps/authenticating-with-github-apps#authenticating-as-a-github-app)
. The script requires the GitHub App ID and the path of the PEM-formatted private key and
generates the encoded JWT token.

# Example usage

```shell
$ ENCODED_JWT_TOKEN=$(GH_APP_ID=<app_id> GH_APP_KEY=<key> python main.py)
$ echo $ENCODED_JWT_TOKEN
```
