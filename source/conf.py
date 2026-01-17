# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Mah-Jong Rules'
copyright = '2026, Wojciech Kozlowski'
author = 'Wojciech Kozlowski'

version = '1.0.0'
release = '1.0.0-1'

html_context = {
    "display_github": True,
    "github_user": "Wojtek242",
    "github_repo": "mahjong-rules",
    "github_version": "main",
    "conf_py_path": "/source/",
}

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_favicon',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

favicons = [
    "favicon/favicon-16x16.png",
    "favicon/favicon-32x32.png",
    "favicon/favicon.svg",
]
