def encaixa(a, b):
    a = str(a)
    b = str(b)
    n = len(b)
    if a[-n:] == b:
        return True
    else:
        return False

def main():
    n = int(input())
    for _ in range(n):
        a, b = input().split()
        print("encaixa" if encaixa(a, b) else "nao encaixa")

if __name__ == "__main__":
    main()