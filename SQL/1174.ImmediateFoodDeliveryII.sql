select ROUND((SUM(CASE tbl.MIN_ORDER_DATE
                       WHEN tbl.CUSTOMER_PREF_DELIVERY_DATE THEN 1 
                       ELSE 0 
                  END )/ COUNT(*))*100, 2) immediate_percentage
from (select *
      from (select d.customer_id, 
                   min(d.order_date) min_order_date
      from Delivery d
      group by d.customer_id) min_order_tbl, 
      Delivery d1
      where min_order_tbl.min_order_date = d1.order_date
      and min_order_tbl.customer_id = d1.customer_id) tbl