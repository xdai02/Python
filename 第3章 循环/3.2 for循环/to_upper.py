str = "Hello World!"

for s in str:
    # 小写字母
    if 97 <= ord(s) <= 122:
        # 转为大写
        upper = ord(s) - 32
        # chr()：将编码转为字符
        print(chr(upper), end='')
    # 
    else:
        print(s, end='')