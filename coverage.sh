# Runs coverage across tests/ and create an HTML report

cd "$(dirname "$0")"
coverage run -m unittest discover tests -v
coverage report
coverage html