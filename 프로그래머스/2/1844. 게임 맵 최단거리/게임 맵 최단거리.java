import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int[][] maps) {
        int[] dx = new int[]{1, -1, 0, 0};
        int[] dy = new int[]{0, 0, -1, 1};
        int n = maps.length;
        int m = maps[0].length;
        
        Queue<int[]> queue = new LinkedList();
        queue.add(new int[]{0, 0, 1});
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;
        
        while(!queue.isEmpty()){
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            int cnt = current[2];
            
            if (x == n-1 && y == m-1){
                return cnt;
            }
            
            for (int i=0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx >= 0 && ny >= 0 && nx < n && ny < m && !visited[nx][ny] && maps[nx][ny] == 1){
                    visited[nx][ny] = true;
                    queue.add(new int[]{nx, ny, cnt +1});
                }
            }
            
        }
        
        return -1;
    }
}
