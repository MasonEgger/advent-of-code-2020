import copy


def run_instructions(instructions):
    acc = 0
    pc = 0
    instruction_order = []
    while pc < len(instructions):
        if pc in instruction_order:
            return acc, -1
        instruction_order.append(pc)
        inst, val = instructions[pc].split(" ")
        if inst == "acc":
            acc += int(val)
            pc += 1
        elif inst == "nop":
            pc += 1
        elif inst == "jmp":
            pc += int(val)

    return acc, 0


def change_nop_jmp(instructions):
    answers = []
    for i in range(0, len(instructions)):
        tmp_instructions = copy.deepcopy(instructions)
        if "nop" in instructions[i]:
            tmp_instructions[i] = "jmp" + "".join(instructions[i][3:])
            answers.append(run_instructions(tmp_instructions))
        elif "jmp" in instructions[i]:
            tmp_instructions[i] = "nop" + "".join(instructions[i][3:])
            answers.append(run_instructions(tmp_instructions))
        else:
            pass

    return answers


if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        instructions = fh.read().split("\n")

    print(run_instructions(instructions))
    mod_instructions = change_nop_jmp(instructions)

    for inst in mod_instructions:
        if inst[1] == 0:
            print(inst[0])
