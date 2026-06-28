def solution(code):
    mode = 0
    ret = ""
    for i in range(len(code)):
        if code[i] == "1":
            mode = 1 - mode                       # "1" 만나면 토글
        else:                                     # "1"이 아니면
            if mode == 0 and i % 2 == 0:          # mode 0 + 짝수
                ret += code[i]
            elif mode == 1 and i % 2 == 1:        # mode 1 + 홀수
                ret += code[i]
    return ret if ret != "" else "EMPTY"          # 빈 문자열이면 EMPTY