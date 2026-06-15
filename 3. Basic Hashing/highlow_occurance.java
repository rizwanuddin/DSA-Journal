import java.util.*;

class highlow_occurance {

    public void Frequency(int[] arr, int n) {
        Map<Integer, Integer> map = new HashMap<>(); // Stores element -> frequency

        // Count frequencies
        for (int i = 0; i < n; i++) {
            map.put(arr[i], map.getOrDefault(arr[i], 0) + 1);
        }

        int maxFreq = 0, minFreq = n;
        int maxEle = 0, minEle = 0;

        // Traverse map to find min and max frequency elements
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int element = entry.getKey();
            int count = entry.getValue();

            if (count > maxFreq) {
                maxFreq = count;
                maxEle = element;
            }

            if (count < minFreq) {
                minFreq = count;
                minEle = element;
            }
        }

        // Print results
        System.out.println("The highest frequency element is: " + maxEle);
        System.out.println("The lowest frequency element is: " + minEle);
    }

    public static void main(String[] args) {
        highlow_occurance fc = new highlow_occurance();
        int[] arr = {10, 5, 10, 15, 10, 5};
        fc.Frequency(arr, arr.length);
    }
}
