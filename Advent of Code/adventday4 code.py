counter = 0

with open("adventday4.txt", "r") as file:
    lines = file.read().splitlines()
    for line in lines:
        cleanLines = map(lines.replace("\n" , "")).replace("\t", "")
    lineSplit = map(str, cleanLines)
    for line in cleanLines:
         if str("XMAS") in lines:
            counter += 1

    printlist = list(cleanLines)
    print(printlist[:10])
       
       
    
    
    print(f"There are a total of {counter} XMASes.")