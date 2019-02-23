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

# Social widget
SOCIAL = (("You can add links in your config file", "#"), ("Another social link", "#"))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

SITESUBTITLE = "Learn. Build. Share."

PROJECTS = [
    {
        "name": "Logpad + Duration",
        "url": "https://github.com/talha131/logpad-plus-duration#logpad--duration",
        "description": "Vim plugin to emulate Windows Notepad logging feature,"
        " and log duration of each entry",
    },
    {
        "name": "Elegant Theme for Pelican",
        "url": "http://oncrashreboot.com/pelican-elegant",
        "description": "A clean and distraction free theme, with search and a"
        " lot more unique features, using Jinja2 and Bootstrap",
    },
]

LANDING_PAGE_ABOUT = {
    "title": "I create tools for learning, building, and sharing.",
    "details": "A dashboard of helpful resources",
}

