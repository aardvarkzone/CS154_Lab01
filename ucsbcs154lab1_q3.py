# ucsbcs154lab1
# All Rights Reserved
# Copyright (c) 2023 Regents of the University of California
# Distribution Prohibited

### Implementing and simulating multiplexers in PyRTL ###

import pyrtl

# Now, it is time to build and simulate (for 16 cycles) a 3-bit 5:1 MUX.
# You can develop your design using either Boolean gates as above or PyRTL's
# conditional assignment.

# Declare five data inputs: a, b, c, d, e
# < add your code here >
a = pyrtl.Input(bitwidth=3, name='a')
b = pyrtl.Input(bitwidth=3, name='b')
c = pyrtl.Input(bitwidth=3, name='c')
d = pyrtl.Input(bitwidth=3, name='d')
e = pyrtl.Input(bitwidth=3, name='e')

# Declare control inputs
s = pyrtl.Input(bitwidth=3, name='s')

# Declare one output: o 
# < add your code here >
o = pyrtl.Output(bitwidth=3, name='o')

# Describe your 5:1 MUX implementation
# < add your code here >
with pyrtl.conditional_assignment:
    with s == 0:
        o |= a
    with s == 1:
        o |= b
    with s == 2:
        o |= c
    with s == 3:
        o |= d
    with s == 4:
        o |= e

# Simulate and test your design for 16 cycles using random inputs
# < add your code here >
sim = pyrtl.Simulation()
sim.step_multiple({'a': [0,1,0,0,0,0], 
                   'b': [0,0,1,0,0,0], 
                   'c': [0,0,0,1,0,0], 
                   'd': [0,0,0,0,1,0], 
                   'e': [0,0,0,0,0,1], 
                   's': [0,1,2,3,4,0]})
sim.tracer.render_trace()