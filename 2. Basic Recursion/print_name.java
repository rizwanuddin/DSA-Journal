//Print a name N times using recursion

public class print_name {
    public void printName(String name, int N, int count){
        if (count == N){
            return;
        }
        System.out.println(name);
        printName(name, N, count+1);
    }
    public static void main(String[] args) {
        print_name solName = new print_name();
        solName.printName("Rizwan", 5, 0);
    }
}

