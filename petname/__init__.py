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


def Adverb():
    return random.choice(adverbs)

def Adjective():
    return random.choice(adjectives)

def Name():
    return random.choice(names)

def Generate(words, separator):
    if words == 1:
        return Name()
    elif words == 2:
        return Adjective() + separator + Name()
    petname = []
    for i in range(0, words - 2):
        petname.append(Adverb())
    petname.append(Adjective())
    petname.append(Name())
    return separator.join(petname)
