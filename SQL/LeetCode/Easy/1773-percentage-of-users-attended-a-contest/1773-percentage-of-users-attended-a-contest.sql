SELECT r.contest_id, 
        ROUND((COUNT(r.user_id)/(SELECT COUNT(UNIQUE(user_id)) 
                            FROM Users))*100, 2) percentage 
FROM Register r
GROUP BY r.contest_id;
ORDER BY percentage DESC, r.contest_id ASC;