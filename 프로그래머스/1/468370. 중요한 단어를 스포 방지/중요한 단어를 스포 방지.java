import java.util.*;

class Solution {
    public int solution(String message, int[][] spoiler_ranges) {
        int n = message.length();

        // 1) 스포 구간 표시 (구간끼리 안 겹치므로 합쳐도 총 길이 ≤ n)
        boolean[] covered = new boolean[n];
        for (int[] r : spoiler_ranges) {
            for (int i = r[0]; i <= r[1]; i++) covered[i] = true;
        }

        // 2) 단어 파싱 + 스포 여부 판정
        List<String> texts = new ArrayList<>();
        List<Boolean> isSpoiler = new ArrayList<>();
        int idx = 0;
        while (idx < n) {
            if (message.charAt(idx) == ' ') { idx++; continue; }
            int start = idx;
            while (idx < n && message.charAt(idx) != ' ') idx++;
            int end = idx - 1;                       // [start, end]

            boolean spoiler = false;
            for (int k = start; k <= end; k++) {
                if (covered[k]) { spoiler = true; break; }
            }
            texts.add(message.substring(start, end + 1));
            isSpoiler.add(spoiler);
        }

        // 3) 비스포 단어 텍스트 집합 (조건 1)
        Set<String> nonSpoilerSet = new HashSet<>();
        for (int w = 0; w < texts.size(); w++) {
            if (!isSpoiler.get(w)) nonSpoilerSet.add(texts.get(w));
        }

        // 4) 왼쪽→오른쪽 순서로 스포 단어 판정
        Set<String> revealed = new HashSet<>();
        int answer = 0;
        for (int w = 0; w < texts.size(); w++) {
            if (!isSpoiler.get(w)) continue;
            String word = texts.get(w);
            if (!nonSpoilerSet.contains(word) && !revealed.contains(word)) {
                answer++;
            }
            revealed.add(word);   // 중요하든 아니든 "공개된 스포 단어"로 기록
        }
        return answer;
    }
}