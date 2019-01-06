#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Joaqim Planstedt'
SITENAME = 'joaqim.github.io'
#SITEURL = 'joaqim.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Stockholm'

DEFAULT_LANG = 'en'

THEME = 'repos/m.css/pelican-theme'
THEME_STATIC_DIR = 'static'

STATIC_PATHS = [
        'images',
        'extra',
        'extra/favicon.ico',
        'extra/robots.txt',
]
EXTRA_PATH_METADATA = {
        'extra/favicon.ico': {'path': 'favicon.ico'},
        'extra/robots.txt': {'path': 'robots.txt'},
}

DIRECT_TEMPLATES = ['index']

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
               '/static/m-dark.css']
M_THEME_COLOR = '#22272e'

M_FAVICON = ('favicon.ico', 'image/x-ico') 
M_BLOG_FAVICON = ('content/favicon-coloured-J-512.png', 'image/png')

PLUGIN_PATHS = ['repos/m.css/pelican-plugins']
PLUGINS = ['m.htmlsanity']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
