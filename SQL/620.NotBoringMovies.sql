/* Write your PL/SQL query statement below */
select tbl.id, tbl.movie, tbl.description, tbl.rating
from (select rownum rn, c.id, c.movie, c.description, c.rating
            from Cinema c
            order by rating desc) tbl
where mod(tbl.rn, 2) != 0
and tbl.description != 'boring';
