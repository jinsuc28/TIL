SELECT p.project_id, ROUND(AVG(NVL(e.experience_years, 0)), 2) average_years
FROM Project p, Employee e
WHERE p.employee_id = e.employee_id(+)
GROUP BY p.project_id;