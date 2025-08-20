// Last updated: 8/20/2025, 5:49:09 PM
class Solution {
    public int addDigits(int num) {
        int x=0;
        while(true)
        {
            int sum = 0;
            while(num!=0)
            {
                sum+=num%10;
                num = num/10;
            }
            if(sum >= 0 && sum<= 9){
                x=sum;
                break;
            }
            else{
                num=sum;
            }
        }
        return x;
        
    }
}