def solution(dartResult):
    answer = 0
    numbers = []
    ind = 0
    for i,x in enumerate(dartResult):
        if x == "S" or x =="D" or x =="T":
            if dartResult[i-2].isdigit():
                if x == "S":
                    numbers.append(int(dartResult[i-2] + dartResult[i-1]))
                elif x == "D":
                    numbers.append(int(dartResult[i-2] + dartResult[i-1])**2)
                else:
                    numbers.append(int(dartResult[i-2] + dartResult[i-1])**3)

            else:
                if x == "S":
                    numbers.append(int(dartResult[i-1]))
                elif x == "D":
                    numbers.append(int(dartResult[i-1])**2)
                else:
                    numbers.append(int(dartResult[i-1])**3)
        elif x == "*" or x =="#":
            if x=="*" and len(numbers) >= 2:
                numbers[-2] *= 2
                numbers[-1] *= 2
            elif x=="*" and len(numbers) == 1:
                numbers[-1] *= 2
            else:
                numbers[-1] = -numbers[-1]
    print(numbers)
    return sum(numbers)
solution("1S2D*3T")
solution("1D2S#10S")
