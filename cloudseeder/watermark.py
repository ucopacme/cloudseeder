#!/usr/bin/env python3
"""
generate a watermark

Usage:
  watermark.py

Arguments:

Option:
  -h        Show this screen.
  -v --version        Show version.
"""

import git
import boto3
from troposphere import Tags


def repo():
    repo = git.Repo(search_parent_directories=True)
    return repo


def gci():
    gci = boto3.client('sts').get_caller_identity()
    return gci


def create_tags(app, env, team, repo):
    tags = Tags(
        app=app,
        env=env,
        team=team,
        repo=repo,
    )
    return tags


def app_env(app, env):
    ae = app + "-" + env
    return ae


def set_desc(template, mesg):
    prefix = "Sceptre managed infrastructure. Please use sceptre to configure the resources in this "
    postfix = " Designed by UCOP Applied Cloud Management and Engineering in Oakland, California. patent pending."
    d = prefix+mesg+postfix
    template.set_description(d)
