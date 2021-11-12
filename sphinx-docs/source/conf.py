import os
import sys
sys.path.insert(0, os.path.abspath('../..'))



project = 'weirdcipher'
copyright = '2021, Federico A. Galatolo'
author = 'Federico A. Galatolo'


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages'
]

exclude_patterns = []
html_theme = 'sphinx_rtd_theme'