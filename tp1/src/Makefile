.PHONY: tests clean
TEST_MODULES = tests.validProductsTest tests.serviceTest

start:
	python startup.py

tests:
	python -m unittest $(TEST_MODULES)

clean:
	rm -f *.pyc
	rm -f tests/*.pyc
