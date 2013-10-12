#!/usr/bin/env bash

function fullpath ()
{
	file="$1"
	dirname=$(dirname "${file}")
	fulldirname=$(cd "${dirname}"; pwd)
	basename=$(basename "${file}")
	echo "${fulldirname}/${basename}"
}

if [ -f "semiautocards.py" ] ; then
	if [ -d "semiauto" ] ; then
		ln -sf "$(fullpath semiautocards.py)" "${HOME}/.anki2/addons/semiautocards.py"
		ln -sf "$(fullpath semiauto)" "${HOME}/.anki2/addons/semiauto"
	fi
fi
