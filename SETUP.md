oc cluster up

oc login developer

oc create -f openshift/templates/django.json

oc new-app openshift/templates/django.json -p SOURCE_REPOSITORY_URL=https://github.com/Seite50/seite50

