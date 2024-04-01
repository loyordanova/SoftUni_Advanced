def create_sequence(n):
    seq = [0, 1]
    for _ in range(n - 2):
        current = seq[-1]
        prev = seq[-2]

        next_num = current + prev
        seq.append(next_num)
    return seq


def locate(number, sequence:list):
    try:
        return f'The number - {number} is at index {sequence.index(number)} '
    except ValueError:
        return f'The number {number} is not in the sequence '


