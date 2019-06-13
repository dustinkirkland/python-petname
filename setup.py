#!/usr/bin/env python3
#
# petname - library for generating human-readable, random names
#           for objects (e.g. hostnames, containers, blobs)
# Copyright (c) 2013 Casey Marshall <casey.marshall@gmail.com>
# Copyright (c) 2019 Dustin Kirkland <dustin.kirkland@gmail.com>
#
# ssh-import-id is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# ssh-import-id is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-petname.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name='petname',
	description='Generate human-readable, random object names',
	long_description=long_description,
	long_description_content_type="text/markdown",
	version='2.6',
	author='Dustin Kirkland',
	author_email='dustin.kirkland@gmail.com',
	license="Apache2",
	keywords="random name uuid",
	url='https://launchpad.net/python-petname',
	platforms=['any'],
	packages=['petname'],
	entry_points={
		'console_scripts': [
			'petname = petname.__main__:main',
		]
	},
)
