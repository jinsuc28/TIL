class Solution {
    public boolean solution(int x) {
        
        String strX = "" + x;
        int sumNum = 0;
        
        for (String s : strX.split("")){
            sumNum += Integer.parseInt(s);
        }
        
        if (x% sumNum == 0){
            return true;
        }
        
        return false;
    }
}