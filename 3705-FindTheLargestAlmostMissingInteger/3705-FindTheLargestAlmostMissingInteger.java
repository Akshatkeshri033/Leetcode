// Last updated: 8/20/2025, 5:48:38 PM
import java.util.*;

class Solution {
    public int largestInteger(int[] nums, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        int n = nums.length;

        // Count occurrences of numbers in all k-sized subarrays
        for (int i = 0; i <= n - k; i++) {
            Set<Integer> seen = new HashSet<>();
            for (int j = i; j < i + k; j++) {
                if (!seen.contains(nums[j])) {
                    freqMap.put(nums[j], freqMap.getOrDefault(nums[j], 0) + 1);
                    seen.add(nums[j]);
                }
            }
        }

        int result = -1;
        // Find the largest number that appears in exactly one subarray
        for (int num : freqMap.keySet()) {
            if (freqMap.get(num) == 1) {
                result = Math.max(result, num);
            }
        }

        return result;
    }
}