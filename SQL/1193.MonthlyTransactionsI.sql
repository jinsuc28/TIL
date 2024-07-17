
select t1.trans_yearMonth_date month, 
       t1.country, 
       count(t1.ID) trans_count,
       sum(t1.approved_state) approved_count,
       sum(t1.amount ) trans_total_amount,
       sum(CASE t1.approved_state
                WHEN 1 THEN t1.amount
                ELSE 0
           END) approved_total_amount
from (select t.id, 
             t.country,
             CASE t.state 
                  WHEN 'approved' THEN 1 
                  ELSE 0 
             END approved_state,
             t.amount, 
             TO_CHAR(trans_date, 'YYYY-MM') trans_yearMonth_date
      from Transactions t) t1
group by t1.trans_yearMonth_date, t1.country
order by t1.trans_yearMonth_date , t1.country DESC;