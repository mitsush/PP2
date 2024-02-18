import json

with open("JSON\sample_data.json", "r") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50, "-" * 20, "-" * 8, "-" * 6)

for x in range(len(data['imdata'])):
    print(data['imdata'][x]['l1PhysIf']['attributes']['dn'], "                              inherit   9150")
    