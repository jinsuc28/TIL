SELECT t.teacher_id, COUNT(DISTINCT t.subject_id) cnt
FROM Teacher t
GROUP BY t.teacher_id;