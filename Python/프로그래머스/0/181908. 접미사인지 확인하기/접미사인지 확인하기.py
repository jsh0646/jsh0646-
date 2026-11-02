def solution(my_string, is_suffix):
    len_suf = len(is_suffix)
    m_s = my_string[-len_suf:]
    if m_s == is_suffix:
        return 1
    else:
        return 0