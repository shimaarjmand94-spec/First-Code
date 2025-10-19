
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

def factorial(n):
    """محاسبه فاکتوریل یک عدد صحیح نامنفی"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# دریافت ورودی از کاربر با مدیریت خطا
while True:
    try:
        user_input = input("لطفاً یک عدد صحیح نامنفی وارد کنید: ")
        n = int(user_input)
        if n < 0:
            print("❌ خطا: عدد باید نامنفی باشد (صفر یا بزرگتر).")
            continue
        break
    except ValueError:
        print("❌ خطا: لطفاً فقط یک عدد صحیح وارد کنید.")

# محاسبه و نمایش نتیجه
result = factorial(n)
print(f"\n{n}! = {result}")
