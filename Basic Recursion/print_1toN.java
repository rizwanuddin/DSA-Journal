//Print numbers from 1 to N using recursion
public class print_1toN {
    public void printNumbers(int N, int current) {
        if (current > N) {
            return;
        }
        System.out.print(current + " ");
        printNumbers(N, current + 1);
    }

    public static void main(String[] args) {
        print_1toN sol = new print_1toN();
        int N = 4;
        sol.printNumbers(N, 1);
    }
}
