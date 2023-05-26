with open("dict_corp_lt.txt", "r") as file:
    lines = file.readlines()

nouns = []

for line in lines:
    if line.find("noun") != -1:
        nouns.append(line)

nouns = list(map(lambda x: x.split(), nouns))

filtered_nouns = []

counter = 0

for line in nouns:
    tags = line[2].split(":")
    if ("fname" in tags) or ("sname" in tags) or ("pname" in tags) or ("prop" in tags) or ("geo" in tags) or ("abbr" in tags) or ("&pron" in tags):
        pass
    else:
        filtered_nouns.append(f"{' '.join(line)}\n")
        counter += 1

with open("filtered_nouns.txt", "w") as file:
    file.writelines(filtered_nouns)

print("FINISHED WRITING FILE")
print(f"Total number of words: {counter}")
