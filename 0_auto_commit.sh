#!/bin/sh
TODAY=`date +%Y%m%d`
COMMIT_LOG="auto commit (${TODAY})"
echo $COMMIT_LOG
git add .
git commit -m "${COMMIT_LOG}"
git push origin master
