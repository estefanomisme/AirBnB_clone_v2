#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder of
an AirBnB Clone repo"""


from datetime import datetime
from fabric.api import local
from os.path import isdir

def do_pack():
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        filename = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except:
        return None
