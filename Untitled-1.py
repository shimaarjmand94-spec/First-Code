
print("سلام دنیا از پروژه من! 🐍")
def factorial(n):
    """محاسبه فاکتوریل یک عدد صحیح نامنفی"""
    if n < 0:
        raise ValueError("فاکتوریل فقط برای اعداد نامنفی تعریف شده است.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(6))