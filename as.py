mysql://pysql:123456@localhost/pysql
connection = connectionForURI('mysql://pysql:123456@localhost/pysql')

##########？？ sqlhub.processConnection = connection


select = Select(staticTables=['person_clone']) # create an instance

select = Select(['fname', 'lname'], staticTables=['person'],groupBy='mi')
>> query = connection.sqlrepr(select)
>> rows = connection.queryAll(query)



class Person(SQLObject):
     firstName = StringCol()
     middleInitial = StringCol(length=1, default=None)
     lastName = StringCol()


query = Person.select()
total = query.count()


peeps = Person.select(OR(Person.q.firstName == "John",LIKE(Person.q.lastName, "%Hope%")))
