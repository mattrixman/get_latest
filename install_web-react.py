#!/usr/bin/python

# Quick script to deploy web-react artifact locally.
# Grabs artifact from artifactory.dev.clover.com
# Expects artifact name , handles service stop/start

import requests
import os
import argparse
import tarfile


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=str, help="The artifact name to deploy (display name in artifactory)")
    parser.add_argument("--url", type=str, default='http://artifactory.corp.clover.com:8081/artifactory/' +
                                                   'ext-release-local/com/clover/web-react/dev/web-react/',
                        help='The report file to create, defaults to http://artifactory.corp.clover.com:8081/' +
                             'artifactory/ext-release-local/com/clover/web-react/dev/web-react/')
    parser.add_argument("--dest", type=str, default='/opt/clover/archive/',
                        help="Destination directory, defaults to /opt/clover/archive/")
    parser.add_argument("--installdir", type=str, default='/opt/clover/web-react', help='where the symlink to ' +
                        'the web-react artifact is created')
    args = parser.parse_args()

    return args


def get_artifact(artifact, base_url, dest_dir):

    print("Downloading artifact " + "web-react" + artifact + ".tar to " + dest_dir)
    full_url = base_url + artifact + '/' + 'web-react-' + artifact + '.tar'
    print("from: " + full_url)
    my_artifact = requests.get(full_url)

    print('writing to:' + dest_dir + 'web-react-' + artifact + '.tar')
    with open(dest_dir + 'web-react-' + artifact + '.tar', 'wb') as output:
        output.write(my_artifact.content)


def control_service(action):

    print("if this were not a test, the web-react service would " + action + " now")


def create_link(artifact, dest_dir, installdir):

    # wow, no force in create symlink...
    print('Linking new artifact')
    try:

        os.remove(installdir)

    except(OSError):

        print('/opt/clover/web-react does not exist, moving on' + OSError.strerror)

    try:

        os.symlink(dest_dir + 'web-react-' + artifact, installdir)

    except(OSError):

        print('cannot link /opt/clover/web-react to artifact, bailing!' + OSError.strerror)
        exit(1)


def unpack_artifact(artifact, dest_dir):

    print('Unpacking artifact')
    tar = tarfile.open(dest_dir + 'web-react-' + artifact + '.tar')
    tar.extractall(path=dest_dir + 'web-react-' + artifact)

    print('setting permissions')

    # since I'm stuck on python 2.7 I cant use os.chowntree and I'm NOT writing
    # some crap iterator...

    try:

        pass # 'cause it's just a test
        #cmdout=os.popen('chown -R payweb:payweb ' + dest_dir + 'web-react-' + artifact).read()

    except(OSError):

        print('Could not set permissions' + OSError.strerror)
        exit(1)


if __name__ == '__main__':

    args = parse_args()

    get_artifact(args.artifact, args.url, args.dest)

    unpack_artifact(args.artifact, args.dest)

    control_service('stop')

    create_link(args.artifact, args.dest, args.installdir)

    control_service('start')
