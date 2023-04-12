# github-app-auth

![Python 3.9](https://img.shields.io/badge/python-3.9-blue)

A simple Python script to authenticate to GitHub as a GitHub App.

The script is based on the Ruby script found in
[Authenticating as a GitHub App](https://docs.github.com/en/developers/apps/building-github-apps/authenticating-with-github-apps#authenticating-as-a-github-app)
. The script requires the GitHub App ID and the path of the PEM-formatted private key and
generates the encoded JWT token.

## Get JWT for a GitHub App

Required environment variables:
- `GH_APP_ID` The GitHub App ID
- `GH_APP_KEY` The path for the GitHub App private key PEM file

```shell
$ GH_APP_ID=<app_id> GH_APP_KEY=<key> python main.py
```

## Get installation access token for a GitHub App

Required environment variables:
- `GH_APP_ID` The GitHub App ID
- `GH_APP_KEY` The path for the GitHub App private key PEM file
- `GH_APP_INST_ID` The GitHub App installation ID

```shell
$ GH_APP_ID=<app_id> GH_APP_KEY=<key> GH_APP_INST_ID=<app_inst_id> python main.py
```
