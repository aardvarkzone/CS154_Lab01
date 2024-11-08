# ucsbcs154lab1
# All Rights Reserved
# Copyright (c) 2023 Regents of the University of California
# Distribution Prohibited

import pyrtl
# Simple example of 1-bit 2:1 mux

val_a = pyrtl.Input(bitwidth=1, name='a')
val_b = pyrtl.Input(bitwidth=1, name='b')
s = pyrtl.Input(bitwidth=1, name='s')
o_wg = pyrtl.Output(bitwidth=1, name='o_wg')

# Important: Assignments inside a "conditional_assignment"
# are done with "|=" instead of the usual "<<="
#with pyrtl.conditional_assignment:
 #with select == 0:
  #  result |= val_a
  #with select == 1:
#    result |= val_b

o_wg <<= (val_b & s) | (val_a & ~s) 

sim = pyrtl.Simulation()
sim.step_multiple({'a': [0,1,0,1], 
                   'b': [0,0,1,1], 
                   's': [0,0,0,1]})
sim.tracer.render_trace()