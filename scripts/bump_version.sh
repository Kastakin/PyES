#!/bin/sh

# display all the arguments using for loop
if [ $# -ne 2 ]
then

  echo "Call the script with current and target vx.x.x version"

else
  tbump $2 &&
  poetry run python scripts/changelog_generator.py v$1 v$2

fi