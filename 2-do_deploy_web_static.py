#!/usr/bin/python3
"""
This script is used to deploy an archive to web servers.
"""

import os
from fabric.api import *

env.hosts = ['34.232.68.81', '54.198.29.36']


def do_deploy(archive_path):
    """
    Uploads the archive to the /tmp/ directory of the web server,
    uncompress the archive to the folder /data/web_static/releases/<archive
    filename without extension> on the web server,
    deletes the archive from the web server,
    deletes the symbolic link /data/web_static/current from the web server,
    creates a new symbolic link /data/web_static/current on the
    web server, linked to the new version of your code.
    Returns:
        bool: True if all operations have been done correctly,
        otherwise returns False
    """
    if not os.path.isfile(archive_path):
        return False
    filename = os.path.basename(archive_path)
    folder = filename.split(".")[0]
    put(archive_path, "/tmp/")
    with cd("/data/web_static/releases/"):
        run("mkdir " + folder)
    with cd("/tmp/"):
        run("tar -xzf " + filename + " -C /data/web_static/releases/" + folder)
    run("rm /tmp/" + filename)
    with cd("/data/web_static/releases/"):
        run("rm -rf current")
        run("ln -s " + folder + " current")
    return True
