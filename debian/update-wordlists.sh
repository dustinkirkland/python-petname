#!/bin/sh

# This script only needs to be run by the upstream package maintainer (Dustin Kirkland)
# if the upstream petname wordlists change

set -e

PKG="petname"

for f in adverbs adjectives names; do
	rm -f "$f".txt.list
	printf "\n$f = [" > "$f".txt.list
	for w in $(cat /usr/share/petname/"$f".txt); do
		printf '"%s", ' "$w" >> "$f".txt.list
	done
	sed -i -e "s/, $/]\n\n/" "$f".txt.list
	sed -i "/^$f = .*$/d" ${PKG}/english.py
done
sed -i -e "/^adjectives = /d" -e "/^adverbs = /d" -e "/^names = /d" -e "/^$/d" ${PKG}/english.py
cat *.txt.list >> ${PKG}/english.py
rm -f *.txt.list
cat /usr/share/doc/petname/README.md > README.md
