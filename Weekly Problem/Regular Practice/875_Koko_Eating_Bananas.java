class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1;
        int r = Integer.MIN_VALUE;
        for(int num : piles) r= Math.max(r, num);
        while(l <= r) {
            int mid = (l+r)/2;
            int time = 0;
            for(int i = 0; i < piles.length; i++) {
                time += Math.ceil((1.0*piles[i]) / mid);
            }
            if(time > h) {
                l = mid+1;
            } else {
                r = mid-1;
            }
        }
        return l;
    }
}
