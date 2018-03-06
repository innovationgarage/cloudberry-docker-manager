import click
import cloudberry_docker_manager.apply
import cloudberry_openwisp
import os.path

CONFIG = os.path.expanduser("~/.config/cloudberry-docker-manager.json")

@click.group()
def main(**kw):
    pass
    
@main.command()
@click.argument("base_url")
@click.argument("uuid")
@click.argument("key")
def init(base_url, uuid, key):
    """Initialize a the docker manager"""
    config = cloudberry_openwisp.Config(CONFIG, base_url, uuid, key)

@main.command()
def update():
    """Update the currently running docker containers with the config from OpenWISP server"""
    config = cloudberry_openwisp.Config(CONFIG)
    config.update()
    cloudberry_docker_manager.apply.apply(config)
