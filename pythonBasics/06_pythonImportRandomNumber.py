import random

# Generate 5 random integers between 1 and 100
for _ in range(5):
    print(random.randint(1, 100))

import random

numbers = random.sample(range(1, 100), 5)  # 1 to 100, 5 unique numbers
print(numbers)

print('>>>>>>>')
import random

numbers = [random.randint(1, 100) for _ in range(5)]
print(numbers)
