set -e
check=""
export PYTHONPATH=$(pwd)
echo $PYTHONPATH
black ${check}  tests processing api
isort ${check}  tests/ processing/ api/
mypy tests processing api
pylint tests/**.py processing api
pytest  tests