# Write your MySQL query statement below
select *
from Users
where  REGEXP_LIKE(mail, '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$', 'c');
#('^[A-Za-z][a-zA-Z0-9_.-]*@leetcode[.]com$')
