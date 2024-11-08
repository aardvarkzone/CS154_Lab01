import pyrtl

A = pyrtl.Input(bitwidth=32, name='A')
B = pyrtl.Input(bitwidth=32, name='B')
result = pyrtl.Output(bitwidth=32, name='result')

A_reg = pyrtl.Register(bitwidth=32, name='A_reg')
B_reg = pyrtl.Register(bitwidth=32, name='B_reg')
counter = pyrtl.Register(bitwidth=32, name='counter')

with pyrtl.conditional_assignment:
    with counter == 0: #base case 1: initializes result = A, loads A_reg
        A_reg.next |= A
        counter.next |= counter + 1
        result |= A
    with counter == 1: #base case 2: initializes result A + B, loads B_reg
        B_reg.next |= B
        counter.next |= counter + 1
        result |= B
    with pyrtl.otherwise: #"recursive" case: updates regs, result
        A_reg.next |= B_reg
        B_reg.next |= A_reg + B_reg
        result |= A_reg + B_reg
        #result |= B_reg.next
        counter.next |= counter + 1

sim = pyrtl.Simulation()
for cycle in range(12):
    sim.step({
        'A':1,
        'B':2
    })
sim.tracer.render_trace()



# think of return as output wire 
# set up registers, set result, increment counter
# registers in memory, wireVectors = pointers 

#result = pyrtl.Output(bitwidth=32, name='result')
#counter = pyrtl.Register(bitwidth=32, name='counter')
#A_counter = pyrtl.Register(bitwidth=32, name='A_counter')
#B_counter = pyrtl.Register(bitwidth=32, name='B_counter')

#counter.next <<= counter + 1

#A_counter.next <<= B
#B_counter.next <<= A



#sim = pyrtl.Simulation()
#sim.step_multiple({'a': [0,1,0,1], 'b': [0,0,1,1], 'result': [0,1,0,1]})
#sim.tracer.render_trace()