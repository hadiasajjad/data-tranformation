select * From employeess;
select first_name, last_name, salary from employeess salary where salary > 500000;
select department, avg(salary) from employeess group by department;
select first_name, last_name, hire_date from employeess where salary between 2022-01-01 and 2022-12-31; 