#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Joaqim Planstedt'
SITENAME = 'www.joaqim.xyz'
SITEURL = 'www.joaqim.xyz'
PATH = 'content'


# Blog
#M_BLOG_NAME = 'Your Brand Blog'
#M_BLOG_URL = 'blog/'
#M_BLOG_FAVICON = ('favicon-blog.png', 'image/png')
STATIC_PATHS = [
        'extra'
        ]
EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
        }

M_FAVICON = ('favicon.ico', 'image/x-ico')


TIMEZONE = 'Europe/Stockholm'

DEFAULT_LANG = 'en'

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

USE_FOLDER_AS_CATEGORY = True
PAGE_PATHS = ['pages']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Top navbar
M_SITE_LOGO_TEXT = 'Joaqim.xyz'

M_LINKS_NAVBAR1 = [
            #('Features', 'features/', 'features', []),
            #('Showcase', 'showcase/', 'showcase', []),
            ('UL', 'ul/', 'ul', []),
            ('Kyuu', 'pages/kyuu', 'kyuu', []) ]

#M_LINKS_NAVBAR2 = [('Blog', 'blog/', '[blog]', [
    #('News', 'blog/news/', ''),
    #('Archive', 'blog/archive/', '')]),
    #('Contact', 'contact/', 'contact', [])]



THEME = 'repos/m.css/pelican-theme'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['index']

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
        '/static/m-dark.css']
M_THEME_COLOR = '#22272e'

PLUGIN_PATHS = [
        'repos/m.css/plugins',
        'repos/'
        ]
PLUGINS = ['m.htmlsanity', 'm.components' ]
M_HTMLSANITY_SMART_QUOTES = True
M_HTMLSANITY_HYPHENATION = True

M_FINE_PRINT = SITENAME + """. Powered by `Pelican <https://getpelican.com>`_
    and `m.css <https://mcss.mosra.cz>`_."""

#M_FINE_PRINT = None
