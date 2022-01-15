#!/usr/bin/python3
"""Fabric module"""


from datetime import datetime
from fabric.api import local, put, run, env
from os.path import isdir, exists

strptime = datetime.strptime
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


def local_clean(number, directory):
    """Deletes unnecessary archives at local server"""
    cmnd = local("ls -1t {}".format(directory), capture=True).split('\n')
    counter = 0
    for q_file in cmnd:
        try:
            if isdir("{}/{}".format(directory, q_file)):
                local("rm -R {}/{}".format(directory, q_file))
            if q_file[:11] != "web_static_":
                local("rm {}/{}".format(directory, q_file))
                continue
            if q_file[-4:] != ".tgz":
                local("rm {}/{}".format(directory, q_file))
                continue
            time = strptime(q_file[11:-4], "%Y%m%d%H%M%S")
            if len(q_file[11:-4]) != 14:
                local("rm {}/{}".format(directory, q_file))
            elif counter >= number:
                local("rm {}/{}".format(directory, q_file))
            else:
                counter += 1
        except ValueError:
            local("rm {}/{}".format(directory, q_file))
            continue


def remote_clean(number, directory):
    """Deletes unnecessary archives at remote servers"""
    cmnd = run("ls -1t {}".format(directory)).split('\r\n')
    counter = 0
    for q_file in cmnd:
        try:
            typefl = run("file {}/{} | cut -d : -f2".format(directory, q_file))
            if typefl != 'directory':
                run("rm {}/{}".format(directory, q_file))
                continue
            if q_file is 'test':
                continue
            if q_file[:11] != "web_static_":
                run("rm -Rf {}/{}".format(directory, q_file))
                continue
            if len(q_file[11:]) != 14:
                run("rm -Rf {}/{}".format(directory, q_file))
                continue
            time = strptime(q_file[11:], "%Y%m%d%H%M%S")
            if counter >= number:
                run("rm -Rf {}/{}".format(directory, q_file))
                continue
            else:
                counter += 1
        except ValueError:
            run("rm -Rf {}/{}".format(directory, q_file))
            continue


def do_clean(number=0):
    """Delete all unnecessary archives at local and remote servers"""
    number = int(number)
    if 0 <= number <= 1:
        first_n_files = 1
    else:
        first_n_files = number
    local_clean(first_n_files, "versions")
    remote_clean(first_n_files, "/data/web_static/releases")
