#!/bin/bash
# Execute tests given the name of test file as first positional argument.
# Tests all *.py test files if no argument is given.

if [ -z "${1+x}" ];
then
	PYFILE='*.py';
else
	PYFILE="$1";
fi

AIRBNB_ENV=test AIRBNB_DATABASE_PWD_TEST='unit_test_pass' \
python -m unittest discover tests/ --pattern="$PYFILE" -v
