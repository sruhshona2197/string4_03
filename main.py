# 1
t = (10, 3, 7, 25, 3)


numbers = [(i, x) for i, x in enumerate(t) if isinstance(x, (int, float))]

if numbers:

    min_index, min_val = min(numbers, key=lambda pair: pair[1])
    max_index, max_val = max(numbers, key=lambda pair: pair[1])

    print(f"Eng kichik: {min_val} (indeks {min_index})")
    print(f"Eng katta: {max_val} (indeks {max_index})")
else:
    print("Tuple ichida son yo'q")


# 2
t = (1, 2, 3, 4, 5, 6)

juft = tuple(x for x in t if x % 2 == 0)
toq = tuple(x for x in t if x % 2 != 0)

print("Juft:", juft)
print("Toq:", toq)


# 3

t = ("salom", "dunyo", "Python", "programming")


strings = [(i, s) for i, s in enumerate(t) if isinstance(s, str)]

if strings:

    index, longest = max(strings, key=lambda pair: len(pair[1]))
    print(f"Eng uzun string: '{longest}' (indeks {index})")
else:
    print("Tuple ichida string yo'q")

# 4
t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')

result = tuple(x for pair in zip(t1, t2) for x in pair)

print(result)


# 5
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5}
s3 = {4, 5, 6}

result = s1 - s2 - s3

print(result)
