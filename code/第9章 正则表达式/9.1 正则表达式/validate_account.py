import re

"""
    验证一个字符串是否是一个合法的账号
    规则：
        1. 纯数字组成
        2. 不能以0开头
        3. 长度[6, 11]
"""

def validate_account(account):
    # 1. 纯数字组成
    if not account.isnumeric():
        return False
    
    # 2. 不能以0开头
    if account.startswith("0"):
        return False
    
    # 3. 长度[6, 11]
    if len(account) < 6 or len(account) > 11:
        return False
    
    return True

def validate_account_with_regex(account):
    # 第1位数字为[1-9]，后面[0-9]可重复5-10次
    return re.match("[1-9]\\d{5,10}", account) != None

def main():
    # 不使用正则表达式
    print(validate_account("2513276112"))
    print(validate_account("012.3"))

    # 使用正则表达式
    print(validate_account_with_regex("h3ll0"))
    print(validate_account_with_regex("28368346"))

if __name__ == "__main__":
    main()