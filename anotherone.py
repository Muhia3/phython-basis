
nums=range(1,10000)
def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

primes = filter(is_prime, range(2, 1001))
print(list(primes))


def main():
 
 for i in range(5):
        print("I love you", end=' ')

if __name__ == "__main__":
    main()

 
a = [1,2,3,4]
a.insert(1, a.pop(2))
print(a)
