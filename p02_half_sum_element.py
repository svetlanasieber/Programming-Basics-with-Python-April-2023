#•	Ако има такъв елемент печата "Yes" и на нов ред "Sum = "  + неговата стойност
#•	Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата между най-големия
# елемент и сумата на останалите (по абсолютна стойност)
import sys

# a.	"max_num" с много ниска първоначална стойност, в която да пазите най-голямото от прочетените числа;
# b.	"sum_numbers" с първоначална стойност 0, в която да пазите сумата от прочетените числа.

# n-на брой цели числа

# 2.	Прочетете броя числа, които ще се въведат на конзолата – n,
# и направете for цикъл от 0 до n, като на всяко завъртане четете число num:


# 3.	Направете проверка дали прочетеното число е по-голямо от "max_num".
# Ако е по-голямо, приравнете стойността на "max_num" към неговата.
# След което добавете стойността на прочетеното число към "sum_numbers





n = int(input())


numbers = [int(input()) for _ in range(n)]

# Calculate the total sum
total_sum = sum(numbers)


found = False

# Check each element
for num in numbers:
    if num == total_sum - num:
        print("Yes")
        print(f"Sum = {num}")
        found = True
        break

# If no such element is found
if not found:
    max_num = max(numbers)
    print("No")
    print(f"Diff = {abs(max_num - (total_sum - max_num))}")



