import random

def main():
    bestTime = 2^21
    bestList = []

    for j in range(10000000):
        i = 0
        clipboard = 0
        time = 0
        previousState = ""
        myList = []

        while i < 1000000:
            ind = random.randint(0,2)
            if ind == 0:
                if previousState == "addOne":
                    i += 1
                    time += 1/30
                else:
                    i += 1
                    time += 1
                    previousState = "addOne"
                myList.append(0)
            elif ind == 1:
                time += 1/2
                clipboard = i
                myList.append(1)
                if previousState == "paste":
                    i += clipboard
                    time += 1/30
                else:
                    i += clipboard
                    time += 1/2
                previousState = "paste"
                myList.append(2)
            elif ind == 2:
                if previousState == "paste":
                    i += clipboard
                    time += 1/30
                else:
                    i += clipboard
                    time += 1/2
                previousState = "paste"
                myList.append(2)

        if time < bestTime:
            bestList = myList
            bestTime = time
    
    print(bestTime)
    print(bestList)