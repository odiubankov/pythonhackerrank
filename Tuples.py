if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tuple_values = ()
    for integer_val in integer_list:
        tuple_values += (integer_val,)
    tuple_hash = hash(tuple_values)
    print(tuple_hash)
