import copy

info = dict(name="Alice", skills=["Python", "C"])
info_copy = copy.deepcopy(info)
info.pop("name")
info_copy["skills"].append("Java")

print(info)
print(info_copy)