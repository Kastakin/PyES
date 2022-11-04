#!/bin/sh
for filename in src/main/python/ui/*.ui; do
    poetry run pyside6-uic $filename -o ${filename%%.*}.py --star-imports
done
poetry run pyside6-rcc src/main/resources/base/resources.qrc -o src/main/python/resources_rc.py
echo "Qt files compiled!"

poetry run python scripts/icon_creator.py
echo "Icons updated!"
