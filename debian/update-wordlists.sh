#!/bin/sh

set -e

PKG="petname"

for f in adverbs adjectives names; do
	rm -f "$f".txt.list
	printf "\n$f = [" > "$f".txt.list
	for w in $(cat /usr/share/petname/"$f".txt); do
		printf '"%s", ' "$w" >> "$f".txt.list
	done
	sed -i -e "s/, $/]\n\n/" "$f".txt.list
	sed -i "/^$f = .*$/d" ${PKG}/__init__.py
done
grep -B 1000 "^import " ${PKG}/__init__.py > above
grep -A 1000 "^def Adverb" ${PKG}/__init__.py > below
cat above *.txt.list below > ${PKG}/__init__.py
rm -f *.txt.list above below
cat /usr/share/doc/petname/README.md > README.md
