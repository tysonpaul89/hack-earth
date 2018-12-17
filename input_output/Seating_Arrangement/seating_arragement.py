# Gets the input count
inputCount = int(input())

# Gets the input data from user
inputData = []
while inputCount != 0:
    inputData.append(int(input()))
    inputCount -= 1

# Calculates the seat numbers
seats = []
even = ['WS', 'MS', 'AS']
odd = ['AS', 'MS', 'WS']
for i in range(1, 108, 3):
    s = None
    if i % 2 == 0:
        s = odd
    else:
        s = even
    x = [j for j in range(i, i+3)]
    seats += list(zip(x, s))
fi = [ k + 5 for k in inputData]
print(fi)