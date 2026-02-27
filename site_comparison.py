import requests
import time 

green = '\033[92m'
red = '\033[91m'

urlA = input("Paste URL here: ")
urlB = input("Paste URL here: ")

listA = []
listB = []

successA = 0
successB = 0

for a in range(5):
    print(f"Connecting to {urlA}...")
    start = time.time()
    response = requests.get(urlA)
    end = time.time()
    duration = (end - start) * 1000
    listA.append(duration)
    averageA = sum(listA) / len(listA)
    if response.status_code == 200:
        successA +=1

for b in range(5):
    print(f"Connecting to {urlB}...")
    start = time.time()
    response = requests.get(urlB)
    end = time.time()
    duration = (end - start) * 1000
    listB.append(duration)
    averageB = sum(listB) / len(listB)
    if response.status_code == 200:
        successB +=1


# print summary 
percentA = (successA / 5) * 100
percentB = (successB / 5) * 100
print("-" * 34)
print(f"Average for Site A: {averageA:.2f}ms | Availability: {percentA}")
print(f"Average for Site B: {averageB:.2f}ms | Availability: {percentB}")

if averageA < averageB:
    diff = averageB - averageA
    print(f"\n{green}Site A is faster by {diff:.2f}ms")
else:
    diff = averageA - averageB
    print(f"\n{green}Site B is faster by {diff:.2f}ms")