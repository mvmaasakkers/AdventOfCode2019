import hashlib

input = "iwrupvqb"
options = [{"first5": hashlib.md5((input + str(x)).encode()).hexdigest()[:5], "first6": hashlib.md5((input + str(x)).encode()).hexdigest()[:6], "hash": hashlib.md5((input + str(x)).encode()).hexdigest(), "number": x} for x in range(1, 10000000)]
print("Part 1:", [x for x in options if x["first5"] == "00000"][0]['number'])
print("Part 2:", [x for x in options if x["first6"] == "000000"][0]['number'])
