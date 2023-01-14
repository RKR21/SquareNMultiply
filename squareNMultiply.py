#Program to do efficient exponentiation
def calculate(a, x, n):
    exponent = bin(x).replace("0b", "")

    solution = a
    for i in range(1, len(exponent)):
        if(exponent[i] == "1"):
            solution = (solution * solution) % n
            solution = (solution * a) % n

        if(exponent[i] == "0"):
            solution = solution * solution % n

    return solution


def main():
    a = 17
    x = 15
    n = 31
    answer = calculate(a, x, n)
    print(answer)
# Answer: 1138812

if __name__ == "__main__":
    main()