#!/usr/bin/python3
"""
This is where the storage engine is initiated
"""


import os


storage_type = os.environ.get("GSPY_TYPE_STORAGE")

if storage_type == "db":
    from models.engine.db_storage import DBStorage

    storage = DBStorage()

storage.reload()
