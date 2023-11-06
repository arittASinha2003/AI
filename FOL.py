from pyDatalog import pyDatalog

# Define the PyDatalog facts for the given atomic sentences
pyDatalog.create_terms('has_leg, likes, brother_of, X, Y, Z')

# John has a leg
+ has_leg('John')

# Raju likes fish
+ likes('Raju', 'fish')

# Raju is the brother of Rani
+ brother_of('Raju', 'Rani')

# Query the facts and print the results
print(has_leg(X))  # Query if someone has a leg
print(likes('Raju', Y))  # Query if Raju likes something and get the result in Y
print(brother_of('Raju', Z))  # Query if Raju is the brother of someone and get the result in Z

from pyDatalog import pyDatalog

# Define some facts
pyDatalog.create_terms('employee, salary')
+ employee('Alice', 50000)
+ employee('Bob', 60000)

# Query data
print(employee(X, Y))  # Query all employees and their salaries

from pyDatalog import pyDatalog

# Define facts and rules
pyDatalog.create_terms('parent, ancestor, X, Y, Z')
+ parent('alex', 'sharon')
+ parent('sharon', 'Charlie')
ancestor(X, Y) <= parent(X, Y)
ancestor(X, Y) <= (parent(X, Z) & ancestor(Z, Y))

# Query for ancestors
print(ancestor(X, 'Charlie'))

from pyDatalog import pyDatalog

# Define some facts
pyDatalog.create_terms('parent1, grandparent')
+ parent1('Alan', 'Bobby')
+ parent1('Bobby', 'ange')
+ parent1('ange', 'Danny')
# Define a rule
grandparent(X, Y) <= (parent1(X, Z) & parent1(Z, Y))
# Query for all grandparents
result = grandparent(X, Y)
print(result)

from pyDatalog import pyDatalog

# Define some facts
pyDatalog.create_terms('age, citizen,can_vote,X,A')
+ age('Alice', 20)
+ citizen('Alice', 'USA')
+ age('JOHN', 10)
+ citizen('Alice', 'USA')

can_vote(X) <= (age(X, A) & citizen(X, 'USA') & (A > 18))
result = can_vote(X)
print(result)

from pyDatalog import pyDatalog

# Define some facts
pyDatalog.create_terms('has, low_stock,X,Q')
+ has('ProductA', 2)
+ has('ProductB', 5)
+ has('ProductC', 15)
low_stock(X) <= (has(X, Q) & (Q < 10))
result=low_stock(X)
print(result)

from pyDatalog import pyDatalog

# Define some facts
pyDatalog.create_terms('enrolled,prerequisite,can_take,X,Y')

+ enrolled('Alice', 'Math101')
+ enrolled('Alice', 'CS101')
+ prerequisite('CS101', 'Math101')
+ prerequisite('Math101', 'Math102')
can_take('Alice', X) <= (enrolled('Alice', Y) & prerequisite(Y, X))
result=can_take('Alice', X)
print(result)

from pyDatalog import pyDatalog

# Define the domain of individuals
pyDatalog.create_terms('king, greedy, evil, X')

# Define the set of individuals who are kings and greedy
+ king('john')
+ greedy('john')
+ king('jack')
+ greedy('jack')
+ king('tom')

evil(X) <= (king(X) & greedy(X))

# Query to find individuals who are both kings and greedy
result = evil(X)
print(result)

from pyDatalog import pyDatalog

pyDatalog.create_terms('student, grade, X,exists')

+ student('Alice')
+ student('Bob')
+ student('Charlie')
+ grade('Alice', 'A')
result = (exists[X], grade(X, 'A'))
print(result)
