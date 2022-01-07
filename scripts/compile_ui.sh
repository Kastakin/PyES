#!/bin/zsh
poetry shell
for filename in src/main/python/ui/*.ui; do
    pyside6-uic $filename -o ${filename%%.*}.py --star-imports
done
pyside6-rcc src/main/resources/base/resources.qrc -o src/main/python/resources_rc.py
echo "Qt files compiled!"
# pipenv run python iconCreator.py
