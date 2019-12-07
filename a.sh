#!/bin/sh

git filter-branch --env-filter '
if [ "$GIT_AUTHOR_NAME" = "朱妍睿" ]
then
export GIT_AUTHOR_NAME="Yanrui Zhu"
export GIT_AUTHOR_EMAIL="yz3705@columbia.edu"
fi
' ref..HEAD

git filter-branch --env-filter '
if [ "$GIT_COMMITTER_NAME" = "朱妍睿" ]
then
export GIT_COMMITTER_NAME="Yanrui Zhu"
export GIT_COMMITTER_EMAIL="yz3705@columbia.edu"
fi
' ref..HEAD