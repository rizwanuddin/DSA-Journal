import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class count_freq{
    public void Frequency(int[] arr, int count){
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i = 0 ; i < count; i++){
            map.put(arr[i], map.getOrDefault(arr[i],0)+1);
        }
        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
        

    }


    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        int count  = scnr.nextInt();
        int [] arr = new int[count];
        for(int i = 0; i < count; i++){
            arr[i] = scnr.nextInt();
        }

    }
}