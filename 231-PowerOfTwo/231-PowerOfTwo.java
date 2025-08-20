// Last updated: 8/20/2025, 5:49:14 PM
class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n<1) return false;
        if(n==1) return true;
        if(n%2==0) return isPowerOfTwo(n/2);
        return false;
    }
}