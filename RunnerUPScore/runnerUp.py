from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    setArr=list(set(list(arr)))
    sortedArr=sorted(setArr)
    lenArr=len(setArr)
    print(sortedArr[lenArr-2])