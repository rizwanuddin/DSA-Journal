import java.util.*;

public class SelectionSort {
    public static void selectionSort(int[] arr){
        int l = arr.length;
        for(int i = 0; i < l-1; i++){
            int minidx = i;
            for(int cur = i + 1; cur < l; cur++ ){
                if(arr[cur] < arr[minidx]){
                    minidx = cur;
                }
            }
            int temp = arr[i];
            arr[i] = arr[minidx];
            arr[minidx] = temp;
        }
    }
    public static void main(String[] args){
        int[] arr = {9, 8, 3, 1, 4, 6, 2};
        selectionSort(arr);
        for(int num : arr){
            System.out.println(num + " ");
        }
    }
}
/*  
Another way to write

import java.util.Arrays;

public class SelectionSortExample {

    public static int[] selectionSort(int[] arr) {
        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;

            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }

            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }

        return arr;
    }
    public static void main(String[] args) {
        int[] arr = {64, 25, 12, 22, 11};

        int[] sortedArr = selectionSort(arr);

        System.out.println(Arrays.toString(sortedArr));
    }
}
*/
