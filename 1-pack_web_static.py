#!/usr/bin/python3
from fabric.api import *
import os
from datetime import datetime

def do_pack():
    try:
        filepath = "versions/web_static_" + datetime.now().strftime("%y%m%d%H%M%S") + ".tgz"
        local("mkdir -p versions")
        local("tar -zcvf version/web_static_$(data +%y%m%d%H%M%S).tgz web_static")
        print("web_static packed: {} -> {}".format(filepath, os.path.getsize(filepath)))
    except BaseException:
        return None
