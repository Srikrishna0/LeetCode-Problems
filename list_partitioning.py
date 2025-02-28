numbers = [0, 1, 2, 3, 4]
chunks = []
chunk_size = 2

while len(numbers) > 0:
  chunks.append(numbers[:chunk_size])
  numbers = numbers[chunk_size:]

chunks