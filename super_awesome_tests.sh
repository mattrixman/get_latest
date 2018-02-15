#! /usr/bin/env bash
LOGFILE="/var/tmp/nightly_web-react.log"

VERSION_INFO=$(find /opt/clover/web-react/ -name gsha| xargs cat)

if [[ -z "$VERSION_INFO" ]] ; then
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] Super Awesome Tests not run.  Software not installed." | tee -a $LOGFILE
else
    VERSION=$(find /opt/clover/web-react/ -name gsha | xargs cat | sed 's/ /\n/g' | awk '/"[0-9a-f]/{print substr($0,2,7)}' | head -n 1)
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] Super Awesome Tests run against version: $VERSION" | tee -a $LOGFILE
fi
