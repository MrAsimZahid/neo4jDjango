from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from neo4janddjango.models.city import City


class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    # Relations :
    city = RelationshipTo(City, 'LIVES_IN')
    friends = RelationshipTo('Person','FRIEND')