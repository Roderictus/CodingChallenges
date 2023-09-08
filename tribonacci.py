def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res

temp = tribonacci([1,2,3], 15)
print(temp)


def tribonacci(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))

    return signature[:n]