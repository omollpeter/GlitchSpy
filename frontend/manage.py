#!/usr/bin/python3
"""
This scripts starts the GlitrchSpy application server
"""

from app import app
from flask.cli import FlaskGroup
import click


cli = FlaskGroup(app)

@cli.command("run")
@click.option("--host", default="0.0.0.0", help="The interface to bind to")
@click.option("--port", default=5050, help="The port to bind to")
def run(host, port):
    """
    Run the Flask server
    """
    # app.run(host=host, port=port)
    from flask.cli import main as flask_main
    import sys
    sys.argv = [sys.argv[0], "run", "--host", host, "--port", str(port)]
    flask_main()

if __name__ == "__main__":
    cli()
