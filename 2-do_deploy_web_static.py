#!/usr/bin/python3
"""A feb file to deploy to a server"""
from fabric.api import *
import os


env.hosts = ['35.190.182.223', '18.232.186.120']

def do_deploy(archive_path):
    a_list = archive_path.split(".tgz")
    archive_wo_ext = "".join(a_list)
    b_list = archive_wo_ext.split("versions/")
    archive_wo_ext_ver = "".join(b_list)
    c_list = archive_path.split("versions/")
    archive_wo_ver = "".join(c_list)
    if archive_path:
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}/".
            format(archive_wo_ext_ver))
        run("tar -zxf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_wo_ver, archive_wo_ext_ver))
        run("rm -r /tmp/{}".format(archive_wo_ver))
        run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/".format(archive_wo_ext_ver,
                                              archive_wo_ext_ver))
        run("rm -rf /data/web_static/releases/{}/web_static".
            format(archive_wo_ext_ver))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(archive_wo_ext_ver))
        print("New version deployed!")
        return True
    else:
        return False
