#!/usr/bin/env bash
"""
Module that contains the prototype def do_pack()
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """generates a .tgz archive from the contents of a folder"""
    try:
        date_time = datetime.now().srtftime("%Y%m%d%H%m%s")
        filename = "web_static_{}".format(date_time)
        local("mkdir -p versions")
        local("tar -cvzf versions/{} ".format(filename))
        return filename
    except:
        return None
