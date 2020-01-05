Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.18 MySQL Community Server - GPL

Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| datarepresentation |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
+--------------------+
6 rows in set (0.00 sec)

mysql> desc databases;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'databases' at line 1
mysql> use test;
Database changed
mysql> desc test;
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int(11)      | NO   | PRI | NULL    | auto_increment |
| name  | varchar(250) | YES  |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+
2 rows in set (0.00 sec)

mysql> use datarepresentation;
Database changed
mysql> use test
Database changed
mysql> show tables;
+----------------+
| Tables_in_test |
+----------------+
| blogposts      |
| test           |
+----------------+
2 rows in set (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| datarepresentation |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
+--------------------+
6 rows in set (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| datarepresentation |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
+--------------------+
6 rows in set (0.00 sec)

mysql> use datarepresentation
Database changed
mysql> show tables;
Empty set (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| datarepresentation |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
+--------------------+
6 rows in set (0.00 sec)

mysql> use datarepresentation
Database changed
mysql> show tables;
Empty set (0.00 sec)

mysql> show tables;
Empty set (0.00 sec)

mysql> use test
Database changed
mysql> show tables
    -> ;
+----------------+
| Tables_in_test |
+----------------+
| blogposts      |
| test           |
+----------------+
2 rows in set (0.00 sec)

mysql> show * blogtables
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '* blogtables' at line 1
mysql> select * blogposts
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'blogposts' at line 1
mysql> SELECT * FROM blogposts
    -> ;
+----+-----------------+-------------------+---------------------------+-------------+
| id | Author_id       | Subject           | Body                      | Total_posts |
+----+-----------------+-------------------+---------------------------+-------------+
|  1 | Emigrant2020    | Living Abroad     | Living in Spain is great  |        NULL |
|  2 | Student2020     | Further Education | Studying at night is hard |        NULL |
|  3 | SportsFan2020   | Favourite Sport   | Football is the best      |        NULL |
|  4 | PoliticsNerd101 | Should I vote?    | Voting is for champions   |        NULL |
|  5 | SportsFan2020   | The FAI           | Sure they are grand!      |        NULL |
+----+-----------------+-------------------+---------------------------+-------------+
5 rows in set (0.02 sec)

mysql> INSERT into blogposts (Author_id, Subject, Body) values ("SportsFan2020", "Euro2020", "Ireland to win!");
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM blogposts;
+----+-----------------+-------------------+---------------------------+-------------+
| id | Author_id       | Subject           | Body                      | Total_posts |
+----+-----------------+-------------------+---------------------------+-------------+
|  1 | Emigrant2020    | Living Abroad     | Living in Spain is great  |        NULL |
|  2 | Student2020     | Further Education | Studying at night is hard |        NULL |
|  3 | SportsFan2020   | Favourite Sport   | Football is the best      |        NULL |
|  4 | PoliticsNerd101 | Should I vote?    | Voting is for champions   |        NULL |
|  5 | SportsFan2020   | The FAI           | Sure they are grand!      |        NULL |
|  7 | SportsFan2020   | Euro2020          | Ireland to win!           |        NULL |
+----+-----------------+-------------------+---------------------------+-------------+
6 rows in set (0.00 sec)