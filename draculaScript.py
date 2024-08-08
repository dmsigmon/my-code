#!/usr/bin/python3

with open("dracula.txt","r") as foo:
    with open("vampytimex.txt", "w") as fang:
        count=0;
        for line in foo:
            if "vampire" in line.lower():
                count++
                print(line);
                fang.write(line)

print(count)

