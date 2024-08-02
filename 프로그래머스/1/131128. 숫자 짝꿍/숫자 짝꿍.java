import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    public String solution(String X, String Y) {

        PriorityQueue<Integer> queueX = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> queueY = new PriorityQueue<>(Collections.reverseOrder());

        for (int idx1 = 0; idx1 < X.length(); idx1++) {
            queueX.add(X.charAt(idx1) - '0');
        }

        for (int idx2 = 0; idx2 < Y.length(); idx2++) {
            queueY.add(Y.charAt(idx2) - '0');
        }

        StringBuilder answer = new StringBuilder();

        while (!queueX.isEmpty() && !queueY.isEmpty()) {
            int numX = queueX.peek();
            int numY = queueY.peek();

            if (numX == numY) {
                answer.append(numX);
                queueX.poll();
                queueY.poll();
            } else if (numX > numY) {
                queueX.poll();
            } else {
                queueY.poll();
            }
        }

        if (answer.length() == 0) {
            return "-1";
        } else if (answer.charAt(0) == '0') {
            return "0";
        } else {
            return answer.toString();
        }
    }
}
