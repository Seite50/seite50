Login: openshift.com


# Einrichten

oc create -f openshift/templates/django.json # Hier kann wahrscheinlich das Openshift Template verwendet werden

oc new-app openshift/templates/django.json -p SOURCE_REPOSITORY_URL=https://github.com/Seite50/seite50

# Fortlaufend
git push ...

oc start-build django-example --from-dir .

# Tutorial für Django
https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1
