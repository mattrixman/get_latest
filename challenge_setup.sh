#! /usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# nuke old versions
rm -rf /opt/clover/archive/*
rm -f /opt/clover/web-react
mkdir -p /opt/clover/archive/none
ln -s /opt/clover/archive/none /opt/clover/web-react

# stage a symlink
rm -f /opt/clover/web-react
ln -s /opt/clover/archive /opt/clover/web-react

# clear the log
rm -f /var/tmp/nightly_web-react.log

# place the script
cp $DIR/install_web-react.py /usr/local/bin/install_web-react
hash -r
