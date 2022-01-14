#!/usr/bin/python3
"""Fabric module"""


from datetime import datetime
from fabric.api import local, put, run, env
from os.path import isdir, exists

env.user = 'ubuntu'
env.hosts = ["35.190.145.109", "54.89.149.139"]


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder of
    an AirBnB Clone repo
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        filename = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception as ex:
        return None


def do_deploy(archive_path):
    """distributes an archive to two web servers"""
    if not exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        f_noext = filename.split(".")[0]
        path = "/data/web_static/releases/"

        put(archive_path, "/tmp/")
        run('sudo mkdir -p {}{}/'.format(path, f_noext))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(filename, path, f_noext))
        run('sudo rm /tmp/{}'.format(filename))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, f_noext))
        run('sudo rm -rf {}{}/web_static'.format(path, f_noext))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(path, f_noext))
        return True
    except BaseException:
        return False

def deploy():
    """creates and distributes an archive to your web servers, using the
    function deploy"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
