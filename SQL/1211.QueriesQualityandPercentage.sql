SELECT q1.query_name, q1.quality, q2.poor_query_percentage
FROM (SELECT query_name, 
             ROUND(AVG(rating / position), 2) quality
      FROM Queries
      WHERE query_name IS NOT NULL
      GROUP BY query_name) q1,
      (SELECT tmp1.query_name, 
              NVL(ROUND((tmp2.poor_count / tmp1.total_count)*100, 2), 0) poor_query_percentage
      FROM (SELECT query_name, COUNT(*) total_count
            FROM Queries 
            GROUP BY query_name) tmp1,
            (SELECT query_name, COUNT(*) poor_count
            FROM Queries 
            WHERE rating < 3
            GROUP BY query_name) tmp2
      WHERE tmp1.query_name = tmp2.query_name(+)) q2
WHERE q1.query_name = q2.query_name(+);

-- 다음부터 가독성과 속도가 좋은 case문을 사용하자
