d = {"a": 3, "b": 1, "c": 2}
result = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

print(result)
