import json

class Primes:

    def __init__(self):
        self.primes = [2]
        try:
            with open("primes.json") as f:
                self.primes = json.load(f)
        except:
            pass

    def generate_more_primes(self, A, output_file_name = "primes.json"):
        start = max(self.primes)
        if A > start:
            end = A
            for val in range(start, end + 1):
                if val > 1:
                    for n in range(2, val // 2 + 2):
                        if (val % n) == 0:
                            break
                        else:
                            if n == val // 2 + 1:
                                self.primes.append(val)
        with open(output_file_name, "w+") as f:
            f.write(json.dumps(self.primes))

    def is_prime(self, a):
        if a in self.primes:
            return True
        return False


if __name__ == "__main__":
    c = Primes()
    print(c.is_prime(11))