#since im not waking up at 5am anymore, i thought i would try use z3 for part 2 since i had a thought that it could work

import z3
A_init, B_init, C_init = 18427963, 0, 0
instructions = [2, 4, 1, 1, 7, 5, 0, 3, 4, 3, 1, 6, 5, 5, 3, 0]

def execute(program, A, B, C):
    def resolve(value):
        return value if value < 4 else [A, B, C][value - 4]
    ip = 0
    output = []
    while ip < len(program):
        op, val = program[ip], program[ip + 1]
        if op == 0:
            A >>= resolve(val)
        elif op == 1:
            B ^= val
        elif op == 2:
            B = resolve(val) % 8
        elif op == 3 and A != 0:
            ip = val
            continue
        elif op == 4:
            B ^= C
        elif op == 5:
            output.append(resolve(val) % 8)
            if len(output) > len(program):
                break
        elif op == 6:
            B = A >> resolve(val)
        elif op == 7:
            C = A >> resolve(val)
        ip += 2
    return ",".join(map(str, output))

result_1 = execute(instructions, A_init, B_init, C_init)
print(result_1)

solver = z3.Solver()
bitvec_size = len(instructions) * 3 + 7
A = z3.BitVec("A", bitvec_size)
original_value = A
X, Y = (b for a, b in zip(instructions[::2], instructions[1::2]) if a == 1)

for target in instructions:
    C = A >> ((A & 7) ^ X)
    B = A ^ X ^ Y ^ C
    solver.add((B & 7) == target)
    A >>= 3

solver.add(A == 0)
while solver.check() == z3.sat:
    solution = solver.model()[original_value].as_long()
    solver.add(original_value < solution)
print(solution)
