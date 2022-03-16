String = '01234567890123456789012345678901234567890123456789'
n = 10
list0 = [String[i:i+n] for i in range(0, len(String), n)]
print('.'.join(list0))

