def generate_carpet(n):
    if n == 0:
        return ["#"]
    else:
        prev_carpet = generate_carpet(n - 1)
        size = len(prev_carpet)
        result = []

        
        for line in prev_carpet:
            result.append(line * 3)
        print("-1")
        print_carpet(result)
       
        for line in prev_carpet:
            result.append(line + "." * size + line)
        print("--2")
        print_carpet(result)
        
        for line in prev_carpet:
            result.append(line * 3)
        print("---3")
        print_carpet(result)

        return result

def print_carpet(carpet):
    for line in carpet:
        print(line)

n = int(input())
carpet = generate_carpet(n)

print(" ")
print("-------answer------")
print_carpet(carpet)