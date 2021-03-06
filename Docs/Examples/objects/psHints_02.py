# example of scaling the hint data.

from robofab.world import CurrentFont

f = CurrentFont()
print f.psHints.asDict()

# a math operation returns a new, unbound object
ps2 = f.psHints * .5       

# it needs to be rounded first
ps2.round()

# now you can add the values to the FL object
f.psHints.update(ps2)

# see those zones skip!
f.update()
