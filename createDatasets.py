
file = open("E:/Joseph-Seminar/vectorscommoncrawlglove.txt", encoding = "utf8")
file1 = open("E:/Joseph-Seminar/vectorscommoncrawlglove3.txt", "w+")

for line in file:
    try:
        words = line.split(" ")
        if words[0].isalpha():
            print(words[0])
            output_string = words[0]
            for j in words[1:]:
                output_string = output_string+" "+ j
            file1.write(output_string)

    except ValueError:
        pass
