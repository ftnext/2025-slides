# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '2025-slides'
copyright = '2025, nikkie'
author = 'nikkie'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages',
    'sphinx_revealjs',
    'sphinx_design',
    'sphinx_new_tab_link',
    'sphinxcontrib.budoux',
    'sphinx_revealjs_copycode',
    'sphinx_revealjs_ext_codeblock',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for Reveal.js output -------------------------------------------------
revealjs_static_path = ["_static"]
revealjs_script_conf = {
    "controls": True,
    "progress": True,
    "history": True,
    "center": True,
    "transition": "none",
    "slideNumber": "c/t",
}
revealjs_script_plugins = [
    {
        "name": "RevealHighlight",
        "src": "revealjs/plugin/highlight/highlight.js",
    },
    {
        "name": "RevealNotes",
        "src": "revealjs/plugin/notes/notes.js",
    },
    {
        "name": "CopyCode",
        "src": "revealjs/plugin/copycode/copycode.js",
    },
]

revealjs_css_files = [
    "revealjs/plugin/highlight/zenburn.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css",
    "css/common.css",
]

# -- Options for sphinxcontrib-budoux -------------------------------------------------
budoux_targets = ["h1", "h2", "h3"]
