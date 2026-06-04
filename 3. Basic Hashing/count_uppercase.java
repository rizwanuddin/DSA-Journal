import java.util.*;
public class count_uppercase{
    public static int[] precompute(String s){
        int[] hash = new int[26];
        /*h i p s (4) so - 0 1 2 3
        0, h - hash[s.chatAt(0)-'A']++ --> hash['h'-'A']++ --> hash[8]++
        1, i -  ....same way te rest 
        */
       for(int i = 0 ; i < s.length(); i++){
        hash[s.charAt(i)-'A']++;
       }
       return hash;
    }
    public static int fetch(int[] hash, char c){
        return hash[c - 'A'];
    }
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in);
        String s = scnr.next();
        int[] hash = precompute(s);
        int q = scnr.nextInt();
        while(q-- > 0){
            char c  = scnr.next().charAt(0);
            System.out.println(fetch(hash, c)); 
        }
    }
}