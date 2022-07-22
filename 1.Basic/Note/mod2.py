def sum(a,b):
    if type(a) != type(b):
        print("더하기를 할 수 없습니다.")
        return
    else:
        return a + b

if __name__ == "__main__": # main method 
    print(sum(10,20))