# delete duplicates but keep one - with unique identifier
# dataframe - employee
# id first_name last_name country
#  1 Raj        Gupta     India
#  2 Raj        Gupta     India
#  3 Mohan      Kumar     USA
#  4 James      Barry     UK
#  5 James      Barry     UK
#  6 James      Barry     UK

# python - drop_duplicates(subset = ['dup_col1', 'dup_col2'])
key = ['first_name', 'last_name', 'country']
employee_clean = employee.drop_duplicates(subset = key)

# sql - delete where id of row_number() > 1
WITH temp AS(
  SELECT id,
         first_name,
         last_name,
         country,
         ROW_NUMBER() OVER(PARTITION BY first_name, last_name, country) AS rn
)
DELETE FROM employee
WHERE id in(
  SELECT id FROM temp WHERE rn > 1
)
