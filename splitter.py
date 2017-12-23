from pathlib import Path

inputFile = Path(input("Enter input file path (e.g. C:\\input.txt) : "))
if inputFile.is_file() == False:
	sys.exit("Wrong path!!")
spCh = input("Enter split character : ")
newCh = input("Enter new character : ")
inputCol = input("Enter column numbers (e.g 1,3,4,7) : ").split(",")
content = open(inputFile, encoding="utf8")
content = content.readlines()
new = []
for i in range(0,len(content)):
	x = content[i].split(spCh)
	row = ""
	for j in range(0,len(x)):
		if str(j) in inputCol:
			row += x[j - 1] + newCh
	row = row[:-1]
	new.append(row + "\n")
outputPath = str(inputFile)
outputPath = outputPath.replace(".txt","_new.txt")
f = open(outputPath, "w",encoding="utf8")
f.writelines(new)
f.close()
print("Transaction successful")
