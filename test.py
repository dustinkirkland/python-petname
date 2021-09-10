import unittest

import petname
import petname.english
from random import Random


class TestAdjective(unittest.TestCase):
	def test_seed(self):
		self.assertEqual(petname.adjective(custom_random=Random(123)),
						petname.adjective(custom_random=Random(123)))

	def test_works(self):
		self.assertIn(petname.adjective(), petname.english.adjectives)

	def test_alias(self):
		self.assertIs(petname.adjective, petname.Adjective)

	def test_len(self):
		for l in range(4, 10):
			self.assertLessEqual(len(petname.adjective(l)), l)


class TestAdverb(unittest.TestCase):
	def test_seed(self):
		self.assertEqual(petname.adverb(custom_random=Random(123)),
						petname.adverb(custom_random=Random(123)))

	def test_works(self):
		self.assertIn(petname.adverb(), petname.english.adverbs)

	def test_alias(self):
		self.assertIs(petname.adverb, petname.Adverb)

	def test_len(self):
		for l in range(4, 10):
			self.assertLessEqual(len(petname.adverb(l)), l)


class TestName(unittest.TestCase):
	def test_seed(self):
		self.assertEqual(petname.name(custom_random=Random(123)),
						petname.name(custom_random=Random(123)))

	def test_works(self):
		self.assertIn(petname.name(), petname.english.names)

	def test_alias(self):
		self.assertIs(petname.name, petname.Name)

	def test_len(self):
		for l in range(4, 10):
			self.assertLessEqual(len(petname.name(l)), l)


class TestGenerate(unittest.TestCase):
	def test_seed(self):
		self.assertEqual(petname.generate(custom_random=Random(123)),
						petname.generate(custom_random=Random(123)))

	def test_works(self):
		words = 3
		sep = '-'
		name = petname.generate(words, sep)
		self.assertEqual(len(name.split(sep)), words)

	def test_alias(self):
		self.assertIs(petname.generate, petname.Generate)


if __name__ == '__main__':
	unittest.main()
