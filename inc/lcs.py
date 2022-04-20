def lcs_fun(word1, word2, w1_len, w2_len):
    """Find the length of Longest Common Substring in two strings.
    Function inspired by code from 
    https://www.geeksforgeeks.org/longest-common-substring-dp-29/"""

    # initalize matrix
    suffix_matrix = [[0 for k in range(w2_len+1)] for l in range(w1_len+1)]

    # length of the longest common substring
    result = 0

    for i in range(w1_len + 1):
        for j in range(w2_len + 1):
            if (i == 0 or j == 0):
                suffix_matrix[i][j] = 0
            elif (word1[i-1] == word2[j-1]):
                suffix_matrix[i][j] = suffix_matrix[i-1][j-1] + 1
                result = max(result, suffix_matrix[i][j])
            else:
                suffix_matrix[i][j] = 0
    return result
