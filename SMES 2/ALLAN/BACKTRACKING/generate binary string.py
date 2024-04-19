from colorama import Fore, Back, Style

def simplified(n):
    
    arr = [None] * n
    
    def print_array(arr,n):
        for i in range(n):
            print(arr[i], end=" ")
        print()

    def generateBinaryString(n, arr, i):
        if i==n:
            print_array(arr,n)
            return
        
        arr[i] = 0
        generateBinaryString(n, arr, i+1)

        arr[i] = 1
        generateBinaryString(n,arr, i+1)
        
    generateBinaryString(n, arr, 0)

def detailed(n):
    
    arr = [None] * n
    
    def print_array(arr,n):
        
        for i in range(n):
            print(Back.LIGHTGREEN_EX+Fore.BLACK,arr[i], end=" "+Style.RESET_ALL)
        print()
        
    def generateBinaryString(n, arr, i):
        blue = Fore.BLUE
        green = Fore.GREEN
        reset = Style.RESET_ALL
        red = Fore.RED
        yelow = Fore.YELLOW
        black = Fore.BLACK
        if i==n:
            print(f"{green}array finished, printing below{reset}")
            print_array(arr,n)
            return

        print(f"{yelow}{i} = i")
        
        arr[i] = 0
        print(f"{blue}array = {arr} | turned arr[{i}] to {0}{reset}")
        print(f"{red}runnung the first recur{reset}")
        generateBinaryString(n, arr, i+1)

        print(f"{Back.RED}on i={i}, passed the first recur{reset}")

        arr[i] = 1
        print(f"{blue}array = {arr} | turned arr[{i}] to {1}{reset}")
        print(f"{red}runnung the second recur{reset}")
        generateBinaryString(n,arr, i+1)
        print(f"{Back.RED}on i={i}, passed the second recur{reset}")

        print("def done")
    generateBinaryString(n, arr, 0)

en = int(input("length : "))
inn = input("detailed or simplified mode? (d/s) ")
if inn == "d":
    detailed(en)
elif inn == "s":
    simplified(en)
else:
    print("error")