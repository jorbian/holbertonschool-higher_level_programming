#!/usr/bin/env python3

user_info = {
    "username": "jorbian",
    "access_token": "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"
}
repo_name = "holbertonschool-higher_level_programming"

template = (
    "https://{}:{}@github.com/{}/{}.git".format(
        user_info["username"],
        user_info["access_token"],
        user_info["username"],
        repo_name
    )
)

print(template)

