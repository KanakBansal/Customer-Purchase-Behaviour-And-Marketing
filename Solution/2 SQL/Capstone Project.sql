create database retail_data;

use retail_data;
select * from marketing_campaign ;

-- Q1
-- Calculate the total number of customer encounters in the marketing campaign dataset
select count(ID) as total_customers from marketing_campaign ;

-- Q2 Important --
-- Identify the top 10 most purchased products in the dataset, such as Wines, Meat Products, etc.
select 
	case
		when product_name = 'MntWines' then 'Wines'
        when product_name = 'MntFruits' then 'Fruits'
		when product_name = 'MntMeatProducts' then 'Meat Products'
        when product_name = 'MntFishProducts' then 'Fish Products'
        when product_name = 'MntSweetProducts' then 'Sweet Products'
        when product_name = 'MntGoldProds' then 'Gold Products'
	end as product_category,
    SUM(product_amount) as total_purchases
from (
	select 
		'MntWines' as product_name,
        MntWines as product_amount
        from marketing_campaign
    union all
	select 
		'MntFruits' as product_name,
        MntFruits as product_amount
        from marketing_campaign
    union all
    select 
		'MntMeatProducts' as product_name,
        MntMeatProducts as product_amount
        from marketing_campaign
    union all
    select 
		'MntFishProducts' as product_name,
        MntFishProducts as product_amount
        from marketing_campaign
    union all
    select 
		'MntSweetProducts' as product_name,
        MntSweetProducts as product_amount
        from marketing_campaign
    union all
    select 
		'MntGoldProds' as product_name,
        MntGoldProds as product_amount
        from marketing_campaign
	) as sub_query
group by product_category
order by total_purchases Desc
limit 10;

-- Q3
-- Find the count of response values
 select 
	response,
    count(*) as Count
from marketing_campaign
group by response;
        
-- Q4
-- Determine the distribution of customers based on their education level and marital status

select 
	Education,
    Marital_Status,
	count(id) as Customer_Count
from marketing_campaign
group by Education, Marital_Status
order by Education, Marital_Status;

-- Q5
-- Identify the average income of customers who participated in the marketing campaign

select avg(income) as Avg_Income
from marketing_campaign;

-- Q6
-- Calculate the total number of promotions accepted by customers in each campaign

select 
	id,
    sum(AcceptedCmp1 + AcceptedCmp2 + AcceptedCmp3 + AcceptedCmp4 + AcceptedCmp5) as Total_no_promotions_accepted
from marketing_campaign
group by id;
	
-- Q7
-- Identify the distribution of customers' responses to the last campaign

select 
    response,
    Count(*)
from marketing_campaign
group by response;

-- Q8
-- Calculate the average number of children and teenagers in customers' households

select 
	avg(kidhome) as Avg_Children,
    avg(teenhome) as Avg_teen
from marketing_campaign;

-- Q9
-- Create an Age column by subtracting year_birth from the current year

alter table marketing_campaign
add Age_new int;

set sql_safe_updates = 0;

update marketing_campaign
set Age_new = year(now())-year_birth;

set sql_safe_updates = 1;

-- Q10
-- Create Age_group columns based on the below condition:
-- WHEN Age BETWEEN 18 AND 25 THEN '18-25'
-- WHEN Age BETWEEN 26 AND 35 THEN '26-35'
-- WHEN Age BETWEEN 36 AND 45 THEN '36-45'
-- WHEN Age BETWEEN 46 AND 55 THEN '46-55'
-- ELSE '56+'

alter table marketing_campaign
add Age_group text;

set sql_safe_updates = 0;

update marketing_campaign 
set Age_group = Case
	WHEN Age BETWEEN 18 AND 25 THEN '18-25'
	WHEN Age BETWEEN 26 AND 35 THEN '26-35'
	WHEN Age BETWEEN 36 AND 45 THEN '36-45'
	WHEN Age BETWEEN 46 AND 55 THEN '46-55'
	ELSE '56+'
end;

set sql_safe_updates = 1;

-- Q11
-- Determine the average number of visits per month for customers in each age group

select 
    Age_group,
    avg(NumWebVisitsMonth) as AvgVisitsPerMonth
from marketing_campaign
group by Age_group
order by Age_group;
