import time


with open("lyrics.txt") as f:
    lyrics = f.read()

lyrics_list = lyrics.split("\n")

for line in lyrics_list:
    print(line)
    time.sleep(len(line) / 5)

num_flying = lyrics.count("날아올라")
print(f"날아오른 횟수: {num_flying}")
