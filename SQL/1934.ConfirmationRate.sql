/* Write your PL/SQL query statement below */

select tmp3.user_id, round(nvl(tmp3.confirmed_sum, 0)/nvl(tmp3.TOTAL, 1),2 ) confirmation_rate
from (select s1.user_id, tmp1.confirmed_sum, tmp2.total
    from Signups s1, (select c2.user_id, count(*) confirmed_sum
            from Confirmations c2
            group by (c2.user_id, c2.action) 
            having c2.action = 'confirmed') tmp1,
            (select c1.user_id, count(*) total
            from Confirmations c1
            group by c1.user_id) tmp2
    where s1.user_id = tmp1.user_id(+)
    and s1.user_id = tmp2.user_id(+)) tmp3