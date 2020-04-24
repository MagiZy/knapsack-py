from gurobipy import *

# define data coefficients
n = 7
p = [6, 5, 8, 9, 6, 7, 3]
w = [2, 3, 6, 7, 5, 9, 4]
c = 9

# create empty model
m = Model()

# add decision variables
# <VARIABLES ADDED HERE>
x = m.addVars(n, vtype=GRB.BINARY, name='x')

# set objective function
# <OBJECTIVE SET HERE>
m.setObjective(x.prod(p), GRB.MAXIMIZE)

# add constraint
# <CONSTRAINT ADDED HERE>
m.addConstr(x.prod(w)<=c, name='knapsack')

# solve model
m.optimize()

# display solution
if m.SolCount > 0:
  m.printAttr('X')

# export model
m.write('knapsack.lp')

