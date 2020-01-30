#!/bin/bash

mkdir -p coverage-reports
echo "######################################################"
echo "                Running tests"
echo "######################################################"
pipenv run pytest test.py

echo "######################################################"
echo "                Running coverage"
echo "######################################################"
pipenv run coverage run test.py
echo "Exporting report"
pipenv run coverage xml -i -o .coverage-reports/coverage-registry.xml
echo "Cleaning up"
pipenv run coverage erase


echo "######################################################"
echo "               Running sonarqube analysis"
echo "######################################################"

source ~/.sonar-scan/auspost
~/Downloads/sonar-scanner/bin/sonar-scanner \
  -Dsonar.login=${SONARTOKEN} \
  $@
