def check(in_list: list, out_list: list) -> bool:
    stack = []
    i = 0
    for num in in_list:
        stack.append(num)
        while stack and stack[-1] == out_list[i]:
            stack.pop()
            i += 1
    return not stack