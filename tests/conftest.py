#!/usr/bin/env python
import os
from time import sleep
import sys
import docker
import pytest
from tests.fixtures import *


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/..'

BROWSER = 'chrome'
SELENIUM_VERSION = '3.4.0'
SELENIUM_IMAGE_NAME = 'selenium/standalone-{browser}:{version}'.format(
        browser=BROWSER,
        version=SELENIUM_VERSION)
SELENIUM_CONTAINER_NAME = 'standalone-{}'.format(BROWSER)


def create_selenium_container(client, network, links=((),)):
    return client.containers.run(
            image=SELENIUM_IMAGE_NAME,
            name=SELENIUM_CONTAINER_NAME,
            ports={'4444': '4444'},
            detach=True,
            networks=[network],
            volumes={
                '/dev/shm': {'bind': '/dev/shm', 'mode': 'rw'}
            },
            links=links,
            environment={'GRID_TIMEOUT': '10'})


def create_webserver_container(client, network):
    return client.containers.run(
            image='python:3.6.1',
            name='webserver',
            hostname='webserver',
            ports={'8000': '8000'},
            detach=True,
            networks=[network],
            volumes={
                PROJECT_DIR + '/tests/index.html': {
                    'bind': '/www/index.html',
                    'mode': 'ro'
                }
            },
            command="""
            bash -c "cd /www && python -m http.server"
            """)


@pytest.fixture(scope='session', autouse=True)
def create_containers_for_tests():
    if 'TRAVIS' in os.environ:
        yield
        return
    client = docker.from_env()
    network = client.networks.create("network1", driver="bridge")
    webserver_container = create_webserver_container(client, network.name)
    selenium_container = create_selenium_container(
            client,
            network.name,
            links=(('webserver', 'webserver'),))
    sleep(1) # Give Selenium some time to wake up.
    yield
    selenium_container.remove(force=True)
    webserver_container.remove(force=True)
    network.remove()
