import java.util.List;
import java.util.ArrayList;

class Solution{
    public int solution(String s){
        List<String> list = new ArrayList<>();
        for (int idx = 0; idx < s.length(); idx++) {
            if (list.size() == 0) {
                list.add("" + s.charAt(idx));
                continue;
            }

            if (!list.get(list.size() - 1).equals("" + s.charAt(idx))) {
                list.add("" + s.charAt(idx));
            } else {
                list.remove(list.size() - 1);
            }
        }
        
        return (list.size() == 0 ? 1 : 0);
    }
}



