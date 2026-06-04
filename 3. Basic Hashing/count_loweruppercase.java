import java.util.*;

class count_loweruppercase {

    static int[] precompute(String s) {
        int[] hash = new int[256];

        for (int i = 0; i < s.length(); i++) {
            hash[s.charAt(i)]++;
        }

        return hash;
    }

    static int fetch(int[] hash, char c) {
        return hash[c];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = sc.next();

        int[] hash = precompute(s);

        int q = sc.nextInt();

        while (q-- > 0) {
            char c = sc.next().charAt(0);
            System.out.println(fetch(hash, c));
        }
    }
}