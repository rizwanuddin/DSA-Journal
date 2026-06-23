public class InsertionSort {
    public static void ShiftinginsertionSort(int[] arr) {
        int n = arr.length;

        for (int i = 1; i < n; i++) {
            int key = arr[i];   // save element to be inserted
            int j = i - 1;

        // shift elements greater than key one position right
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }

            arr[j + 1] = key;   // place key in correct spot
        }
    }
    public static void swappingInsertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int j = i;

            while (j > 0 && arr[j - 1] > arr[j]) {

                // swap
                int temp = arr[j];
                arr[j] = arr[j - 1];
                arr[j - 1] = temp;

                j--;
            }
        }

        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}