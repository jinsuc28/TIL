class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # 해쉬맵 만들기
        hash_map = {src:[] for src, _ in tickets}
        tickets.sort()
        for src, dst in tickets: hash_map[src].append(dst)

        res = ["JFK"]
        def dfs(src):
            # ticket 사용한 것 + 1이 방문 지역 길이
            if len(res) == len(tickets) + 1:
                return True
            if src not in hash_map:
                return False

            tmp = list(hash_map[src])
            for i, v in enumerate(tmp):
                hash_map[src].pop(i)
                res.append(v)
                if dfs(v): return True
                hash_map[src].insert(i, v)
                res.pop()

            return False

    
        dfs("JFK")
        return res
    