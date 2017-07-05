#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Carioca HackerSpace'
SITENAME = 'Carioca HackerSpace'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME='themes/bricks'
#THEME='pelican-bootstrap3'
#BOOTSTRAP_THEME = 'flatly'

# Pelican Github Projects
PLUGINS = [
#    'sitemap',
    'pelican_githubprojects'
]


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/CariocaHackerSpace/'),
          ('github', 'https://github.com/CariocaHS"'),)

DEFAULT_PAGINATION = 10

# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = True

# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = True

# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU = False

# Display the category in the article's info
#DISPLAY_CATEGORIES_ON_POSTINFO (False)

# Display the author in the article's info
#DISPLAY_AUTHOR_ON_POSTINFO (False)

# Display the search form
#DISPLAY_SEARCH_FORM (False)

# Sort pages list by a given attribute
#PAGES_SORT_ATTRIBUTE (Title)

# Display the "Fork me on Github" banner
GITHUB_URL = "https://github.com/CariocaHS"
GITHUB_USER = 'kura'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
