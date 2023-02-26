# Data_Manipulation
```sql
/* employee
id first_name last_name country rn
1  Raj        Gupta     India   1
2  Raj        Gupta     India   2
3  Mohan      Kumar     USA     1
4  James      Barry     UK      1
5  James      Barry     UK      2
6  James      Barry     UK      3
*/
```
**Delete Duplicates - SQL**
<br>delete where id of row_number() > 1
```sql
WITH temp AS(
  SELECT id,
         first_name,
         last_name,
         country,
         ROW_NUMBER() OVER(PARTITION BY first_name, last_name, country) AS rn
  FROM employee
)
DELETE FROM employee
WHERE ID in(
  SELECT id FROM temp WHERE rn > 1
)
```
