"""
The flask application package.
"""

from flask import Flask
from werkzeug.contrib.cache import FileSystemCache
from verifier import settings

app = Flask(__name__)
app.config.from_pyfile("settings.py")
cache = FileSystemCache(settings.APP_CACHE)

from verifier.modules.helpers import setup_logging
setup_logging(settings.APP_LOGS, 
              "verifier.log", 
              settings.LOG_LEVEL_FILE,
              settings.LOG_LEVEL_CONSOLE)

import modules.context_processor
import verifier.views
from verifier.modules import helpers










