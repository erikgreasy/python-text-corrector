from inc.lcs import lcs_fun
from inc.editing_distance import edit_distance


def optimize_text_lcs(input_string, dictionary_string, output_file_name):
    """Transform corrupted input string with LCS function using
    the dicionary passed as argument. The corrected string is
    returned but also writtes to file."""

    input_array = input_string.split()
    dictionary = dictionary_string.split()

    # CORRECT TEXT
    corrected_output = []

    for word in input_array:
        longest = 0
        norm_word = word.lower()

        corrected_word = None

        for dict_word in dictionary:
            if norm_word == dict_word:
                corrected_word = norm_word
                break

            substr_len = lcs_fun(norm_word, dict_word,
                                 len(norm_word), len(dict_word))

            if substr_len > longest:
                longest = substr_len
                corrected_word = dict_word

                if substr_len == len(word):
                    break

        print(corrected_word)
        corrected_output.append(corrected_word)
        corrected_word = None

    # WRITE CORRECTED STRING TO OUTPUT FILE
    write_output_to_file(corrected_output, output_file_name)

    return corrected_output


def optimize_text_editing_distance(input_string, dictionary_string, output_file_name):
    """Transform corrupted input string with Edit Distance function using
    the dicionary passed as argument. The corrected string is
    returned but also writtes to file."""

    input_array = input_string.split()
    dictionary = dictionary_string.split()

    # CORRECT TEXT
    corrected_output = []

    for word in input_array:
        least_operations = 2147483647
        norm_word = word.lower()

        corrected_word = None

        for dict_word in dictionary:
            if norm_word == dict_word:
                corrected_word = norm_word
                break

            operations = edit_distance(
                norm_word, dict_word, len(norm_word), len(dict_word))

            if operations < least_operations:
                least_operations = operations
                corrected_word = dict_word

        print(corrected_word)
        corrected_output.append(corrected_word)
        corrected_word = None

    # WRITE CORRECTED STRING TO OUTPUT FILE
    write_output_to_file(corrected_output, output_file_name)

    return corrected_output


def write_output_to_file(output_array, output_file_name):
    output_string = ''
    output_file = open(output_file_name, "w")

    for word in output_array:
        output_string += word + ' '

    output_file.write(output_string)

    output_file.close()
