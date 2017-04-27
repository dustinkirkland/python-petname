#  petname: library for generating human-readable, random names
#           for objects (e.g. hostnames, containers, blobs)
#
#  Copyright 2014 Dustin Kirkland <dustin.kirkland@gmail.com>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import random
from .english import adverbs, adjectives, names


try:
	random = random.SystemRandom()
except NotImplementedError:
	pass # less secure

def adverb(letters=6):
	while 1:
		w = random.choice(adverbs)
		if len(w) <= letters:
			return w


def adjective(letters=6):
	while 1:
		w = random.choice(adjectives)
		if len(w) <= letters:
			return w


def name(letters=6):
	while 1:
		w = random.choice(names)
		if len(w) <= letters:
			return w


def generate(words=2, separator="-", letters=6):
	if letters < 3:
		letters = 3
	if words == 1:
		return name(letters)
	elif words == 2:
		return adjective(letters) + separator + name(letters)
	petname = []
	for i in range(0, words - 2):
		petname.append(adverb(letters))
	petname.append(adjective(letters))
	petname.append(name(letters))
	return separator.join(petname)


# aliases for backwards compatiblity
Adverb = adverb
Adjective = adjective
Name = name
Generate = generate
