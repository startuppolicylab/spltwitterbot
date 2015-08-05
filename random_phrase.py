import random
import time

class random_word:
	def __init__(self):
		self.ubers = open('uber.txt', 'r')
		self.nouns = open('nouns.txt', 'r')
		self.verbs = open('verbs.txt', 'r')
		self.adjectives = open('adjectives.txt', 'r')
	def noun(self):
		self.nouns.seek(0)
		lines = self.nouns.readlines()
		return random.choice(lines).rstrip()
	def verb(self):
		self.verbs.seek(0)
		lines = self.verbs.readlines()
		return random.choice(lines).rstrip()
	def adjective(self):
		self.adjectives.seek(0)
		lines = self.adjectives.readlines()
		return random.choice(lines).rstrip()
	def uber(self):
		self.ubers.seek(0)
		lines = self.ubers.readlines()
		return random.choice(lines).rstrip()


def random_phrase(phrase, a):
	if phrase == 1:
		return "You need to %s the %s in order to %s the %s %s. #startupadvice" % (a.verb(), 
			a.noun(), a.verb(), a.adjective(), a.noun())
	elif phrase == 2:
		return "In order to %s, you are going to have to %s the %s %s. #startupadvice" % (a.verb(), 
			a.verb(), a.adjective(), a.noun())
	elif phrase == 3:
		return "If you want a %s %s, you need to %s the %s. #startupadvice" % (a.adjective(), 
			a.noun(), a.verb(), a.noun())
	elif phrase == 4:
		return "It's like Uber but for %s. It is going to be %s! #startupadvice" % (a.uber(), a.adjective())
	elif phrase == 5:
		return "Go and %s the %s! It's the only way to %s a real %s. #startupadvice" % (a.verb(),
			a.noun(), a.verb(), a.noun())
	elif phrase == 6:
		return "Your startup will fail unless you %s and %s the %s %s. #startupadvice" % (a.verb(),
			a.verb(), a.adjective(), a.noun())

	
# while True:
# 	foo = random_word()
# 	random_phrase(random.randint(1,6), foo)
# 	time.sleep(10)
