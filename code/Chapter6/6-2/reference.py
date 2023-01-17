info = dict(name="Alice", skills=["Python", "C"])
info_ref = info
info_ref["skills"].append("Java")
print(info)