"""Sphinx configuration."""
from datetime import datetime


project = "Spring Boot `/actuator/env` difffing"
author = "Ties de Kock"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "sphinx_rtd_theme",
]
autodoc_typehints = "description"
html_theme = "sphinx_rtd_theme"
