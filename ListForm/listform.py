from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    N = int(input())

List=[]
for s in range(N):
    input = raw_input().strip().split(" ")
    if input[0]=="append":
        List.append(int(input[1]))
    elif input[0]=="insert":
        List.insert(int(input[1]),int(input[2]))
    elif input[0]=="remove":
        List.remove(int(input[1]))
    elif input[0]=="sort":
        List.sort()
    elif input[0]=="pop":
        List.pop()
    elif input[0]=="reverse":
        List.reverse()
    elif input[0]=="print":
        print(List)