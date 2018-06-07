def swap_case(s):
    new_str = ""
    for i in range(0, len(s)):
        new_str += s[i].upper() if s[i].lower() == s[i] else s[i].lower()
    return new_str
