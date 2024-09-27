def decode_message(s: str, p: str) -> bool:
    s_len = len(s)
    p_len = len(p)
    
    # Pointers for message and pattern
    s_index, p_index = 0, 0
    # To track the last position of '*' in p
    star_index = -1
    # To track the position in s where we will resume matching after '*'
    match_index = 0
    
    while s_index < s_len:
        # If characters match or there's a '?' in pattern, move both pointers
        if p_index < p_len and (p[p_index] == s[s_index] or p[p_index] == '?'):
            s_index += 1
            p_index += 1
        # If we encounter a '*', record its position and try to match it
        elif p_index < p_len and p[p_index] == '*':
            star_index = p_index
            match_index = s_index
            p_index += 1
        # If there's a mismatch but a previous '*' exists, backtrack
        elif star_index != -1:
            p_index = star_index + 1
            match_index += 1
            s_index = match_index
        # Mismatch without any '*' to backtrack to
        else:
            return False
    
    # If there are remaining characters in the pattern, they should all be '*'
    while p_index < p_len and p[p_index] == '*':
        p_index += 1
    
    return p_index == p_len
