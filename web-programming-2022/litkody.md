---
description: Решение 6 лит задач.
---

# Литкоды

### Задача 1: Find the team size. база данных №1303

```
+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| employee_id   | int     |
#| team_id       | int     |
#+---------------+---------+
```

employee\_id is the primary key for this table. Each row of this table contains the ID of each employee and their respective team. Write an SQL query to find the team size of each of the employees. Return result table in any order.

#### Решение:

```sql
SELECT em.employee_id,
       sub.total team_size
FROM Employee em
JOIN (
  SELECT team_id, COUNT(*) total
  FROM Employee
  GROUP by team_id) sub ON sub.team_id = em.team_id;
```

### Задача 2: Rectangle Area #223

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

### Задача 3: Convert a Number to Hexadecimal №405

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

### Задача 4: Remove Element №27

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

### Задача 5: Merge two sorted lists №21

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

### Задача 6: Letters combinaitions of a phone number №17

<figure><img src="../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>
