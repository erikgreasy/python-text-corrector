def edit_distance(word1, word2, w1_len, w2_len):
    """Find edit distance value for two strings. Function inspired
    by code from https://www.geeksforgeeks.org/edit-distance-dp-5/?ref=gcse"""

    # Create empty matrix
    ed_matrix = [[0 for x in range(w2_len + 1)] for x in range(w1_len + 1)]

    for i in range(w1_len + 1):
        for j in range(w2_len + 1):

            # word1 empty, insert all chars of word2
            if i == 0:
                ed_matrix[i][j] = j

            # word2 empty, remove all chars of word2
            elif j == 0:
                ed_matrix[i][j] = i

            # last chars same, ignore last char
            # and recur for remaining string
            elif word1[i-1] == word2[j-1]:
                ed_matrix[i][j] = ed_matrix[i-1][j-1]

            # last chars different, consider all
            # possibilities and find minimum
            else:
                ed_matrix[i][j] = 1 + min(
                    ed_matrix[i][j-1],  # Insert
                    ed_matrix[i-1][j],  # Remove
                    ed_matrix[i-1][j-1]  # Replace
                )

    return ed_matrix[w1_len][w2_len]
