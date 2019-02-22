#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Carol Willing"
SITENAME = "pysplash.io"
SITEURL = ""

PATH = "content"
TIMEZONE = "America/Los_Angeles"

DEFAULT_LANG = "en"

THEME = "theme"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PROJECTS = (
    ("Python.org", "http://python.org/"),
    ("Jupyter", "http://jupyter.org/"),
    ("nteract", "http://nteract.io/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (("You can add links in your config file", "#"), ("Another social link", "#"))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

SITESUBTITLE = "Learn. Build. Share."
