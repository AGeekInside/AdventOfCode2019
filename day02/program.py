import sys


def next_command(intprogram):
    """Returns the next command of the provided intprogram"""
    instruction_pointer = 0
    max_address = len(intprogram)

    while instruction_pointer < max_address:
        command_end = instruction_pointer + 4
        current_command = intprogram[instruction_pointer:command_end]
        instruction_pointer = command_end
        yield current_command


def process_command(command, program):

    # print(f"Processing {command}")
    # print(f"OPCODE - {command[0]}")

    value1 = program[command[1]]
    value2 = program[command[2]]
    if command[0] == 99:
        #print("Found end. Printing current program state:")
        #print(program)
        return
    elif command[0] == 1:
        new_value = value1 + value2
    elif command[0] == 2:
        # print(f"Multiplying {value1} to {value2}.")
        new_value = value1 * value2

    # print(f"RESULT : {new_value}")
    # print(f"Writing {new_value} to {command[3]}")
    program[command[3]] = new_value


def process_program(program):

    # print(f"About to process {program}")

    for i, command in enumerate(next_command(program)):
        # print(f"About to process {i} th command: {command}")
        if command[0] == 99:
            break
        process_command(command, program)

    # print(f"Final program {program}")


def run_intprogram():

    test_programs = [
        [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
        [1, 0, 0, 0, 99],
        [2, 3, 0, 3, 99],
        [2, 4, 4, 5, 99, 0],
        [1, 1, 1, 4, 99, 5, 6, 0, 99],
    ]

    for test_program in test_programs:
        process_program(test_program)

    input_file = "./day02/input_day02.csv"

    intprogram = []

    with open(input_file) as input:
        raw_program = input.readline().strip()
        intprogram = [int(cmd) for cmd in raw_program.split(",")]

    for noun in range(99):
        for verb in range(99):
            work_program = intprogram.copy()
            work_program[1] = noun
            work_program[2] = verb
            process_program(work_program)
            output = work_program[0]

            if output == 19690720:
                print(f"Inputs: noun : {noun}, verb: {verb}")
                print(f"Solution: {100 * noun + verb}")


if __name__ == "__main__":
    run_intprogram()
