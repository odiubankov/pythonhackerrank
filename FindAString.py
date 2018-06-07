def count_substring(string, sub_string):
    equal_cnt = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        equal = True
        for j in range(0, len(sub_string)):
            if string[i + j] != sub_string[j]:
                equal = False;
                break
        if equal:
            equal_cnt += 1
    return equal_cnt

if __name__ == '__main__':
    count_substring("ABCDCDC", "CDC")
