// Last updated: 8/20/2025, 5:48:32 PM
class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        int a=mainTank;
       while(mainTank>=5 && additionalTank>0){
        a+=1;
        mainTank+=1;
        mainTank-=5;
        additionalTank-=1;
       }
       return a*10;
       
    }
}