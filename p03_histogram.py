

n = int(input())


count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0


for _ in range(n):
    num = int(input())
    if num < 200:
        count_p1 += 1
    elif 200 <= num <= 399:
        count_p2 += 1
    elif 400 <= num <= 599:
        count_p3 += 1
    elif 600 <= num <= 799:
        count_p4 += 1
    else:
        count_p5 += 1


print(f"{count_p1 / n * 100:.2f}%")
print(f"{count_p2 / n * 100:.2f}%")
print(f"{count_p3 / n * 100:.2f}%")
print(f"{count_p4 / n * 100:.2f}%")
print(f"{count_p5 / n * 100:.2f}%")

# Тази програма първо инициализира броячите за всеки от петте диапазона
# като count_p1, count_p2, count_p3, count_p4 и count_p5.
# След това прочита n-те числа, като актуализира съответния брояч за всяко число.
#
# Накрая се изчисляват процентите,
# като всеки брояч се разделя на n и се умножава по 100,
# а след това се отпечатват с два знака след десетичната запетая.
