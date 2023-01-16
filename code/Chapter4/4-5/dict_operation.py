info = {"name": "Terry"}
print("info =", info)

info.update({"age": 24, "height": 179.2})
print("update() =", info)

print("keys() =", info.keys())
print("values() =", info.values())

print("get('age') = ", info.get("age"))

info.pop("height")
print("pop('height') =", info)

info.popitem()
print("popitem() =", info)

info.clear()
print("clear() =", info)