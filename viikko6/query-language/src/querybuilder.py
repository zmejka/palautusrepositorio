from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, query = All()):
        self.query_object = query

    def build(self):
        return self.query_object

    def playsIn(self, attr):
        return QueryBuilder(And(self.query_object, PlaysIn(attr)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query_object, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query_object, HasFewerThan(value, attr)))

    def oneOf(self, *queues):
        return QueryBuilder(Or(*queues))
