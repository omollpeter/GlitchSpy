#!/usr/bin/python3
"""
This scripts starts the GlitchSpy application server
"""

from frontend.app import app


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
