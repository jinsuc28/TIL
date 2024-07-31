import java.util.Map;
import java.util.HashMap;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        Map<String, Integer> map = new HashMap<>();
        int nameLength = name.length;
        int photoLength = photo.length;
        int Score = 0;
        
        int[] resultArr = new int[photoLength];
        
        for (int idx=0; idx<nameLength; idx++){
            map.put(name[idx], yearning[idx]);
            Score += yearning[idx];
        }
        
        System.out.println(map);
        for (int idx1=0; idx1<photoLength; idx1++){
            int photoScore = 0;
            
            for (int idx2=0; idx2<photo[idx1].length; idx2++){
                
                try{
                photoScore += map.get(photo[idx1][idx2]);
                }
                catch(Exception e){
                }
                
            }
            resultArr[idx1] = photoScore;
        }

        return resultArr;
    }
}