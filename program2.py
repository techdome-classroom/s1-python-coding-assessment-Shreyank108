def decode_message(s: str, p: str) -> bool:
    # Pointers for the message and pattern
    s_index, p_index = 0, 0
    # To track the last position of '*' in p
    star_index = -1
    # To track the position in s where we will continue matching after '*'
    match_index = 0
    
    while s_index < len(s):
        # If characters match or we have a '?', move both pointers
        if p_index < len(p) and (s[p_index] == s[s_index] or p[p_index] == '?'):
            s_index += 1
            p_index += 1
        # If we encounter a '*', record the position and try to match
        elif p_index < len(p) and p[p_index] == '*':
            star_index = p_index
            match_index = s_index
            p_index += 1
        # If there's a mismatch but we encountered a '*', backtrack
        elif star_index != -1:
            p_index = star_index + 1
            match_index += 1
            s_index = match_index
        else:
            return False
    
    while p_index < len(p) and p[p_index] == '*':
        p_index += 1

    return p_index == len(p)