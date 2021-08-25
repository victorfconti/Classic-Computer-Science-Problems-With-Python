from stack import Stack

num_disk: int = 3

tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

for i in range(1, num_disk + 1):
    tower_a.push(i)

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int):
    if n == 1:
        end.push(begin.pop)
    else:
        hanoi(begin, temp, end, n-1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n-1)

if __name__ == "__main__":
    hanoi(tower_a, tower_b, tower_c, num_disk)
    print(tower_a)
    print(tower_b)
    print(tower_c)