from sympy import symbols, Not, And, Or, Implies, Equivalent,simplify

# Define propositional variables
p, q, r = symbols('p q r')

#NOT (Negation):
not_p = Not(p)

#AND (Conjunction):
p_and_q = And(p, q)

#OR (Disjunction):
p_or_q = Or(p, q)

#IMPLIES (Implication):
p_implies_q = Implies(p, q)

#EQUIVALENT (Equivalence):
p_biimplies_q = Equivalent(p,q)

print("negation",not_p)
print("Conjunction",p_and_q)
print("Disjunction",p_or_q)
print("Implication",p_implies_q)
print("biimplies",p_biimplies_q)

# Substitute truth values
truth_values = {p: True, q: False,r:True}
pandq = p_and_q.subs(truth_values)
porq = p_or_q.subs(truth_values)
notp = not_p.subs(truth_values)
pimpliesq = p_implies_q.subs(truth_values)
pbiimpliesq = p_biimplies_q.subs(truth_values)

print("negation",notp)
print("Conjunction",pandq)
print("Disjunction",porq)
print("Implication",pimpliesq)
print("BIImplication",pbiimpliesq)

print(Not(And(p,q)).subs(truth_values))

from sympy.logic.boolalg import truth_table
var=[p,q]
expr1=p_and_q
expr2=p_or_q
expr3=not_p
expr4=p_implies_q
expr5=p_biimplies_q
print("AND")
tt1 = truth_table(expr1,var)
for row1 in tt1:
    print(row1)

print("OR")
tt2 = truth_table(expr2,var)
for row2 in tt2:
    print(row2)

print("NOT")
tt3 = truth_table(p,var)
for row3 in tt3:
    print(row3)

print("IMPLIES")
tt4 = truth_table(expr4,var)
for row4 in tt4:
    print(row4)

print("BIIMPLIES")
tt5 = truth_table(expr5,var)
for row5 in tt5:
    print(row4)

s,t,u=symbols('s t u')
t1 = truth_table(And(s,t,u),[s,t,u])
print(list(t1))

from sympy import pprint

pprint(p_or_q, use_unicode=True)
pprint(p_and_q, use_unicode=True)
pprint(not_p, use_unicode=True)
pprint(p_biimplies_q, use_unicode=True)

from sympy import simplify

expr = Or(And(p, q), And(p, r))
simplified_expr = simplify(expr)
print(expr)
print(simplified_expr)

from sympy import Equivalent
print("Demorgan's Law")
expr1 = Not(And(p, q))
expr2 = Or(Not(p), Not(q))
Demorganequiv = Equivalent(expr1, expr2)
print(Demorganequiv)
print(simplify(Demorganequiv))

print("Contraposition  Law")

expr3=Implies(p,q)
expr4=Implies(Not(q),Not(p))
contrapositionequiv = Equivalent(expr3, expr4)
print(contrapositionequiv)
print(simplify(contrapositionequiv))

from sympy import symbols, Not, And, Or, Implies, Equivalent
from sympy.logic.boolalg import to_cnf

# Define symbolic variables
p, q, r = symbols('p q r')


# Apply and display logical equivalence rules to original expressions
print("Rule 1: De Morgan's Laws")
rule1_result = to_cnf(Not(And(p, q)))
print("Result:", rule1_result)
print()

print("Rule 2: Distribution (AND over OR)")
rule2_result = to_cnf(Or(p, And(q, r)))
print("Result:", rule2_result)
print()

print("Rule 3: Implication Elimination")
rule3_result = to_cnf(Implies(p, q))
print("Result:", rule3_result)
print()

print("Rule 4: Bi-Implication Elimination")
rule4_result = to_cnf(Equivalent(p, q))
print("Result:", rule4_result)
print()

print("Rule 5: Double Negation")
rule5_result = to_cnf(Not(Not(p)))
print("Result:", rule5_result)
print()

print("Rule 6: Idempotent Law")
rule6_result = to_cnf(Or(p, p))
print("Result:", rule6_result)
print()


print("Rule 7: Negation of True and False")
rule7_result = to_cnf(Not(True))
print("Result:", rule7_result)
print()
rule8_result = to_cnf(Not(False))
print("Result:", rule8_result)
print()

from sympy import to_cnf, to_dnf

expr = Equivalent(p,Or(q,r))
cnf_expr = to_cnf(expr)
dnf_expr = to_dnf(expr)
print(expr)
print(cnf_expr)
print(dnf_expr)

from sympy import symbols, Not, Or, And, to_cnf, Equivalent

# Define the propositional variables
B1_1, P1_2, P2_1 = symbols('B1_1 P1_2 P2_1')

# Define the original formula R2
R2 = Equivalent(B1_1, Or(P1_2, P2_1))

# Convert R2 to CNF
cnf_R2 = to_cnf(R2, True)

# Print the CNF expression for R2
print(cnf_R2)

from sympy import symbols, Implies

# Define symbolic variables
A, B = symbols('A B')

# Define the premise and conclusion
premise = A
conclusion = Implies(A, B)

# Check if the premise entails the conclusion
entails = not (premise and (not conclusion))


# Print the result
print("The premise entails the conclusion:", entails)

from sympy import symbols, Implies, And

# Define symbolic variables
W11, S12 = symbols('W11 S12')

# Define the knowledge base (rules)
knowledge_base = [
    Implies(W11, S12),  # If there's a Wumpus in (1, 1), there's a stench in (1, 2)
]

# Check if the knowledge base holds for the given case
case_holds = all(rule.subs({W11: True, S12: True}) for rule in knowledge_base)

print("The knowledge base holds for the given case:", case_holds)

from sympy import symbols, Implies, And, Or, Not

# Define symbolic variables for pits in locations (1, 2), (2, 2), and (3, 1)
P12, P22, P31 = symbols('P12 P22 P31')

# Define symbolic variables for breezes in adjacent locations
B11, B13, B21, B23, B32, B33 = symbols('B11 B13 B21 B23 B32 B33')

# Define the knowledge base rules
knowledge_base_rules = [
    Implies(P12, Or(B11, B13)),  # If there's a pit in (1, 2), there's a breeze in (1, 1) or (1, 3)
    Implies(P22, Or(B21, B23, B32)),  # If there's a pit in (2, 2), there's a breeze in (2, 1), (2, 3), or (3, 2)
    Implies(P31, Or(B32, B33)),  # If there's a pit in (3, 1), there's a breeze in (3, 2) or (3, 3)

    # Rule to ensure there is no pit in (1, 2)
    Not(P12)
]

# Check if the knowledge base holds for the given case
knowledge_base_holds = all(rule for rule in knowledge_base_rules)

# Print the result of the entailment check
print("The knowledge base entails 'there is no pit in (1, 2)':", knowledge_base_holds)

from sympy import symbols, And, Not, Or, Implies, Equivalent, satisfiable

# Define symbolic variables
p, q, r = symbols('p q r')

# Define a propositional logic formula
# Replace this formula with the one you want to check for validity
formula = Or(p,Not(p))
#formula = Implies(p,q) #invalid formula
# Check if the formula is valid
is_valid = True

# Generate all possible truth assignments for the variables
for p_value in (True, False):
    for q_value in (True, False):
        # Evaluate the formula under the current truth assignment
        current_assignment = {p: p_value, q: q_value}
        if not formula.subs(current_assignment):
            # If the formula is false for any assignment, it's not valid
            is_valid = False
            break

# Display the result
if is_valid:
    print("The formula is valid.")
else:
    print("The formula is not valid.")

from sympy import symbols, And, Not, Or, Implies, Equivalent, satisfiable

# Define symbolic variables
p, q, r = symbols('p q r')

# Define a propositional logic formula
# Replace this formula with the one you want to check for satisfiability
formula=And(p,q)
#formula = And(p,Not(p)) #unsatisfiable formula

# Check if the formula is satisfiable
satisfiable_assignment = satisfiable(formula)

if satisfiable_assignment:
    print("The formula is satisfiable.")
    print("Satisfying assignment:", satisfiable_assignment)
else:
    print("The formula is not satisfiable.")
