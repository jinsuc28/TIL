import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;        // 맵의 행 크기
        int m = maps[0].length;     // 맵의 열 크기
        
        // 상하좌우 방향을 나타내는 배열 (동, 서, 남, 북)
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        
        // BFS를 위한 Queue 초기화 및 시작점 추가
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {0, 0});
        
        // 방문 시작
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            
            // 네 방향으로 이동
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                // 맵을 벗어나지 않는지, 벽이 아닌지 확인
                if (nx >= 0 && ny >= 0 && nx < n && ny < m && maps[nx][ny] == 1) {
                    // 방문하지 않은 곳이라면
                    maps[nx][ny] = maps[x][y] + 1; // 거리 갱신
                    queue.add(new int[] {nx, ny});
                }
            }
        }
        
        // 상대팀 진영 (n-1, m-1)에 도착할 수 있는지 확인
        return maps[n-1][m-1] > 1 ? maps[n-1][m-1] : -1;
    }
}
