import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    public String solution(String X, String Y) {
        // PriorityQueue는 기본적으로 최소 힙을 사용하므로, 큰 숫자가 먼저 나오게 하기 위해 Collections.reverseOrder()를 사용합니다.
        PriorityQueue<Integer> queueX = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> queueY = new PriorityQueue<>(Collections.reverseOrder());

        // X의 숫자를 우선순위 큐에 추가
        for (int idx1 = 0; idx1 < X.length(); idx1++) {
            queueX.add(X.charAt(idx1) - '0');
        }

        // Y의 숫자를 우선순위 큐에 추가
        for (int idx2 = 0; idx2 < Y.length(); idx2++) {
            queueY.add(Y.charAt(idx2) - '0');
        }

        StringBuilder answer = new StringBuilder();

        // 두 큐가 모두 비어 있지 않을 때까지 반복
        while (!queueX.isEmpty() && !queueY.isEmpty()) {
            int numX = queueX.peek();
            int numY = queueY.peek();

            if (numX == numY) {
                // 두 숫자가 같으면 결과에 추가하고 큐에서 제거
                answer.append(numX);
                queueX.poll();
                queueY.poll();
            } else if (numX > numY) {
                // X의 숫자가 크면 Y의 큐에서 제거
                queueX.poll();
            } else {
                // Y의 숫자가 크면 X의 큐에서 제거
                queueY.poll();
            }
        }

        // 결과 문자열이 비었거나 0으로만 구성된 경우 처리
        if (answer.length() == 0) {
            return "-1";
        } else if (answer.charAt(0) == '0') {
            return "0";
        } else {
            return answer.toString();
        }
    }
}
