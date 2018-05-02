Login: openshift.com


# Einrichten
oc create -f openshift/templates/django.json

oc new-app openshift/templates/django.json -p SOURCE_REPOSITORY_URL=https://github.com/Seite50/seite50

# Fortlaufend
git push ...

oc start-build django-example --from-dir .