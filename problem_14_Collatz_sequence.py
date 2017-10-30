from time import clock

limit = 1000000
longest_chain = 1
longest_chain_for_number = 1
found_chains_length = {1: 1}

start = clock()
for number in range(2, limit):
    current_number = number
    counter = 1
    if number % 100000 == 0:
        print(number)
    while current_number != 1:
        if current_number % 2 == 0:
            current_number /= 2
        else:
            current_number = current_number * 3 + 1

        if current_number in found_chains_length:
            counter += found_chains_length[current_number]
            found_chains_length[number] = counter
            break

        counter += 1

    if counter > longest_chain:
        longest_chain = counter
        longest_chain_for_number = number

print(longest_chain_for_number)
print(clock() - start)
