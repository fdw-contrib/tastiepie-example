from tastypie.resources import ModelResource
from restful_app.models import Person


class PersonResource(ModelResource):
    class Meta:
        queryset = Person.objects.all()
        resource_name = 'person'