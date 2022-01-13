#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
from fabric.api import *
import os
from datetime import datetime


def do_pack():
    """archives the static file"""
    try:
        filepath = "versions/web_static_" + datetime.now().\
            strftime("%Y%m%d%H%M%S") + ".tgz"
        local("mkdir -p versions")
        local("tar -zcvf versions/web_static_$(date +%Y%m%d%H%M%S).tgz\
     web_static")
        print("web_static packed: {} -> {}".
              format(filepath, os.path.getsize(filepath)))
    except BaseException:
        return None
