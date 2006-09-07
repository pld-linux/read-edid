#!/bin/sh
#
# Copyright (c) 2004 Colin Watson <cjwatson@debian.org>.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

set -e

TREE=/proc/device-tree

# Apparently some 2.4 kernels put OF aliases in aliases@0.
if [ -d /proc/device-tree/aliases ]; then
	ALIASES=aliases
elif [ -d /proc/device-tree/aliases@0 ]; then
	ALIASES=aliases@0
else
	echo "Can't find Open Firmware aliases directory" >&2
	exit 2
fi

if [ -f "$TREE/$ALIASES/screen" ]; then
	SCREEN="`cat $TREE/$ALIASES/screen`"
else
	echo "Can't find Open Firmware screen alias" >&2
	exit 2
fi

# Aliases start with a slash.
if [ -d "$TREE$SCREEN" ]; then
	EDID=
	# List gathered from files in drivers/video/ in the 2.6.7 kernel
	# source.
	for file in DFP,EDID LCD,EDID EDID EDID1 EDID2 EDID,B EDID,A; do
		if [ -f "$TREE$SCREEN/$file" ]; then
			EDID="$TREE$SCREEN/$file"
			break
		fi
	done
	if [ -z "$EDID" ]; then
		echo "Can't find EDID file in $TREE$SCREEN" >&2
		exit 1
	fi
else
	echo "Can't find target of Open Firmware screen alias ($TREE$SCREEN)" >&2
	exit 2
fi

cat "$EDID"
