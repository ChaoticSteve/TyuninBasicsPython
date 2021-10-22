src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

next_more = [num_after for num, num_after in zip(src, src[1:]) if num_after > num]
print(next_more)
