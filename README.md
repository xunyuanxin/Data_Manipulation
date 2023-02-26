# Data_Manipulation
```sql
/* employee
id first_name last_name country
1  Raj        Gupta     India
2  Raj        Gupta     India
3  Mohan      Kumar     USA
4  James      Barry     UK
5  James      Barry     UK
6  James      Barry     UK
*/
```
**Delete Duplicates** 
- SQL: 
  - delete where id of row_number() > 1
- Python: 
  - key features: <br>`employee.drop_duplicates(subset = ['first_name', 'last_name', 'country'])`
  - all features: drop unique identifer first<br>`employee.drop('id', axis = 1).drop_duplicates()`
****
