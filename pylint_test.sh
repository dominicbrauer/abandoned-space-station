# This shell script runs pylint over the source and
# tests directories using the custom .pylintrc-file

cd "$(dirname "$0")"
rcfile="./.pylintrc"

pylint --rcfile=$rcfile ./src/
pylint --rcfile=$rcfile ./tests/ # not necessary in this case
