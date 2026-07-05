# Write your MySQL query statement below
-- select 
-- case 
--     when income<20000 then 'Low Salary'
--     when income between 20000 and 50000 then 'Average Salary'
--     when 50000<income then 'High Salary' 
-- end as category,
-- count(account_id) as accounts_count
-- from Accounts
-- group by category


select 
    'Low Salary' as category,
    count(*) as accounts_count
    from Accounts
    where income<20000
union all
select 
    'Average Salary' as category,
    count(*) as accounts_count
    from Accounts
    where income between 20000 and 50000
union all
select 
    'High Salary' as category,
    count(*) as accounts_count
    from Accounts
    where 50000<income