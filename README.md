import json as j

# the data in another file
data = j.loads("""
{
    "id":101,
    "Course":"ML",
    "status":"Completed"
}
""")

with open("data.json", "w") as f:
    j.dump(data, f, indent=4)
    
with open("data.json", "r") as f:
    data1 = j.load(f)

results = {
    "status": data1["status"]
}

with open("results.json", "w") as f:
    j.dump(results, f)

    
print(data1)
print(j.dumps(data1, indent=4, sort_keys=True))



# TODO: Load config.json from disk
# TODO: Print config values
# TODO: Create results dict and write to results.json

# Hint: use Path and with open(...)
