def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    stacks = []
    procedure = []
    current_stack = []
    for line in lines:
        line = line.strip()
        if line.startswith('['):
            current_stack = [crate[1] for crate in line.split()]
            stacks.append(current_stack)
        elif line.startswith('move'):
            parts = line.split()
            procedure.append((int(parts[1]), int(parts[3]), int(parts[5])))

    return stacks, procedure

def rearrange_crates(stacks, procedure):
    # Parse the initial configuration of the stacks
    stacks = [list(stack) for stack in stacks]

    # Execute the rearrangement procedure
    for step in procedure:
        num_crates, src, dest = step
        src -= 1  # Convert to 0-based indexing
        dest -= 1  # Convert to 0-based indexing
        while len(stacks) <= dest:
            stacks.append([])
        crates = []
        for _ in range(num_crates):
            if src < len(stacks) and stacks[src]:  # Check if the src stack is not empty
                crates.append(stacks[src].pop())
        stacks[dest] = crates + stacks[dest]  # Insert the crates at the bottom of the destination stack

    # Get the top crate of each stack
    top_crates = [stack[-1] if stack else '' for stack in stacks]

    # Combine the top crates to form the final message
    message = ''.join(top_crates)

    return message

def main():
    stacks, procedure = parse_input('data.txt')
    message = rearrange_crates(stacks, procedure)
    print(message)

if __name__ == "__main__":
    main()