"""
This is where the storage engine is initiated
"""

from models.engine.db_storage import DBStorage


storage = DBStorage()
storage.reload()
