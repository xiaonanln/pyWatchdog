.PHONY: all build test clean

all: build test

build: 
	python setup.py build

test: build
	python tests/testPyWatchdog/test.py

