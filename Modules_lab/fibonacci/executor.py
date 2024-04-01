from fibonacci_helpers import create_sequence, locate


def play_fibonacci():
    command = input()
    sequence = []
    while command != 'Stop':
        if command.startswith('Create'):
            n = int(command.split()[-1])
            sequence = create_sequence(n)
            print(*sequence)
        else:
            m = int(command.split()[-1])
            print(locate(m, sequence))
        command = input()