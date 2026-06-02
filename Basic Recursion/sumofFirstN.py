class SumOfFirst:
    def SumOfFirstN(self, N, current, total):
        if current > N:
            print(total)
            return

        total += current
        self.SumOfFirstN(N, current + 1, total)


if __name__ == "__main__":
    sol = SumOfFirst()
    N = 5
    sol.SumOfFirstN(N, 1, 0)