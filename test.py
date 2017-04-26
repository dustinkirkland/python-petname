import unittest

import petname
import petname.english


class TestAdjective(unittest.TestCase):
	def test_works(self):
		self.assertIn(petname.adjective(), petname.english.adjectives)

	def test_alias(self):
		self.assertIs(petname.adjective, petname.Adjective)

	def test_len(self):
		for l in range(4, 10):
			self.assertLessEqual(len(petname.adjective(l)), l)


class TestAdverb(unittest.TestCase):
	def test_works(self):
		self.assertIn(petname.adverb(), petname.english.adverbs)

	def test_alias(self):
		self.assertIs(petname.adverb, petname.Adverb)

	def test_len(self):
		for l in range(4, 10):
			self.assertLessEqual(len(petname.adverb(l)), l)


class TestName(unittest.TestCase):
	def test_works(self):
		self.assertIn(petname.name(), petname.english.names)

	def test_alias(self):
		self.assertIs(petname.name, petname.Name)

	def test_len(self):
		for l in range(4, 10):
			self.assertLessEqual(len(petname.name(l)), l)


class TestGenerate(unittest.TestCase):
	def test_works(self):
		words = 3
		sep = '-'
		name = petname.generate(words, sep)
		self.assertEqual(len(name.split(sep)), words)

	def test_alias(self):
		self.assertIs(petname.generate, petname.Generate)


if __name__ == '__main__':
	unittest.main()
