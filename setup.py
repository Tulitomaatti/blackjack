try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Blackjack in python for Javalabra2013',
	'author': 'Tulitomaatti',
	'url': 'https://github.com/Tulitomaatti/blackjack',
	'author_email': 'tulitomaatti+python@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['blackjack'],
	'scripts': [],
	'name': 'blackjack'
}

setup(**config)
