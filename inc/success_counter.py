def success_counter(string_array_1, string2):
    correct_count = 0
    total = len(string_array_1)

    array1 = string_array_1
    array2 = string2.split()

    for i in range(total):
        if array1[i] == array2[i]:
            correct_count += 1

    print(f'success {correct_count}/{total}: {correct_count/total}')
    # print(len(string1.split()))
    # print(len(string2.split()))
