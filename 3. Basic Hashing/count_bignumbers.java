import java.util.*;
public class count_bignumbers {
    public static HashMap<Integer, Integer> precompute(int[] arr, int count){
        HashMap<Integer, Integer> mp = new HashMap<>();
        for(int i = 0; i < arr.length; i++){
            int key = arr[i];
            int freq = 0;
            if (mp.containsKey(key)){
                freq = mp.get(key);
            }
            freq ++;
            mp.put(key, freq);
        }

        return mp;
    }
    public static int fetch(HashMap<Integer, Integer> mp, int num ){
        if(mp.containsKey(num)){
            return mp.get(num);
        }    
        return 0 ;
    }   
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in);
        int count = scnr.nextInt();
        int[] arr = new int[count];
        for(int i = 0; i < count; i++){
            arr[i] = scnr.nextInt();
        }
        HashMap<Integer, Integer> mp = precompute(arr, count);

        int q = scnr.nextInt(); //the number of numbers you want count for
        while(q-- > 0){
            int num = scnr.nextInt();
            System.out.println(fetch(mp, num));
        }

    }
}
