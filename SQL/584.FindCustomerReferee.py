SELECT name FROM Customer
WHERE referee_id != 2 OR referee_id is null;

# upvode solution
SELECT name 
FROM customer
WHERE referee_id <> 2 OR referee_id IS NULL

# <> 와 != 는 같은 의미의 연산자이다.