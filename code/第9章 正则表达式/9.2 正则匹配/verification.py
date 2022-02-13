import re

def main():
    # 1. 验证QQ账号：长度5-11，首位不为0
    print(re.match("[1-9]\\d{4,10}", "2513276112"))

    # 2. 验证QQ邮箱：QQ号码@qq.com
    print(re.match("[1-9]\\d{4,10}@qq\\.com", "2513276112@qq.com"))

    # 3. 验证手机号
    print(re.match("1[356789]\\d{9}", "13671712345"))

    # 4. 验证固定电话：区号（3-4位）-电话号码（8位）
    print(re.match("\\d{3,4}-\\d{8}", "021-55031234"))

    # 验证126或163邮箱：邮箱名（4-12位有效字符）@126/163.com
    print(re.match("\\w{4,12}@(126|163)\\.com", "admin123@163.com"))
    
if __name__ == "__main__":
    main()