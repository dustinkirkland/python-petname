#!/usr/bin/env python3
#
# petname - library for generating human-readable, random names
#           for objects (e.g. hostnames, containers, blobs)
# Copyright (c) 2013 Casey Marshall <casey.marshall@gmail.com>
# Copyright (c) 2019 Dustin Kirkland <dustin.kirkland@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup
import io

try:
	with io.open("README.md", "r", encoding='utf-8') as fh:
		long_description = fh.read()
except UnicodeDecodeError:
	long_description = str()

setup(
	name='petname',
	description='Generate human-readable, random object names',
	long_description=long_description,
	long_description_content_type="text/markdown",
	version='2.9',
	author='Dustin Kirkland',
	author_email='dustin.kirkland@gmail.com',
	license="Apache2",
	keywords="random name uuid",
    url='https://github.com/dustinkirkland/python-petname',
	platforms=['any'],
	packages=['petname'],
	package_data={'petname': ['py.typed']},
	entry_points={
		'console_scripts': [
			'petname = petname.__main__:main',
		]
	},
)
