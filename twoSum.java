import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap= new HashMap<>();
        int[] indices = new int[2];
        
        
        for(int i = 0; i < nums.length; i++) {
            if(numMap.containsKey(target - nums[i])) {
                indices[0] = i;
                indices[1] = numMap.get(target - nums[i]);
                return indices;
            }
            numMap.put(nums[i], i);
        }
        
        return null;
    }
}