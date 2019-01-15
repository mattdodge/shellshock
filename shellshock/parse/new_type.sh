#!/bin/sh
PARSECLASS=$1
PARSETYPE=$2
lowertype=`echo $PARSETYPE | awk '{print tolower($0)}'`

echo $PARSECLASS
echo $lowertype

PARSETYPE=$PARSETYPE envsubst < _template.py > $PARSECLASS/$lowertype.py

echo "from .$lowertype import ${PARSETYPE}Type" >> $PARSECLASS/__init__.py
