select product_id, nvl(round(sum(price*units)/sum(units), 2), 0) average_price
from (select p.product_id,
            p.price, 
            us.units
    from Prices p, UnitsSold us
    where p.product_id = us.product_id(+)
    and nvl(p.start_date - us.purchase_date , 0) <=0
    and nvl(us.purchase_date - p.end_date, 0) <= 0)
group by product_id;