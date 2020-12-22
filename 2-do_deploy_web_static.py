#!/usr/bin/python3
"""
Module that contains do_deploy
"""
from os import path
from fabric.api import env, run, put, local


env.hosts = ['34.74.102.184', '	34.75.178.150']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """deploys archive to server"""

    if not path.isfile(archive_path):
        return False

    file_archive = archive_path.split('/')[1]
    file_no_ext = archive_file.split('.')[0]
    releases = '/data/web_static/releases/{}/'.format(no_file_ext)

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(releases))
        run('tar -xzf /tmp/{} -C {}'.format(file_archive, releases))
        run('rm /tmp/{}'.format(file_archive))
        run('mv {}/web_static/* {}'.format(releases, releases))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases))
        return True
    except Exception as e:
        return False
