SELECT ROUND((SUM(CASE tbl.MIN_ORDER_DATE
                       WHEN tbl.CUSTOMER_PREF_DELIVERY_DATE THEN 1 
                       ELSE 0 
                  END )/ COUNT(*))*100, 2) immediate_percentage
FROM (SELECT *
      FROM (SELECT d.customer_id, 
                   MIN(d.order_date) min_order_date
      FROM Delivery d
      GROUP BY d.customer_id) min_order_tbl, 
      Delivery d1
      WHERE min_order_tbl.min_order_date = d1.order_date
      AND min_order_tbl.customer_id = d1.customer_id) tbl