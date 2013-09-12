Usage after nose has been installed:

run
nosetests -v
in project root folder (folder containing blackjack, tests, setup.py, docs, bin, README.md

For now the tests are in nosetest to meet the deadline requirements for testing. 
I'll study the python's builtin testing tools and convert all test to those later on if needed.

For now it looks like virtualenv provides an easy enough way to run these on department computers. 
Something like:

virtualenv foo
source foo/bin/activate
pip install nose

Should suffice to create an environment for running the tests. 
