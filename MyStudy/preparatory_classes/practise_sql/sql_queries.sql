-- 0. Retrieve all rows and all columns of employee table

-- 0. Retrieve First name and last name of ALL employees




-- 1. Retrieve details of all male employees who draw a salary which is at least 30000

-- 2. Retrieve the details of all dependents of essn 333445555

-- 3. Retrieve details of projects that are based out Houston or Stafford

-- 4. Retrieve details of projects that are based out Houston or belongs
--    to deptartment 4

-- 5. Display the name of the department and the year in which the manager
--    was appointed (Hint: Use the YEAR() function YEAR(mgr_start_date)

-- 6. Display the SSN of all employees who live in Houston
--    (Hint: use LIKE() function as in address LIKE '%Houston'
-- 6. Display employees whose name begins with J

-- 7. Display details of all (male employee who earn more than 30000) or female employees who earn less than 30000)

-- 8. Display the essn of employees who have worked betwen 25 and 50 hours
--      a) Use AND clause
--      b) use BETWEEN clause  as in Hours between 25 and 30




-- 9. Display the names of projects that are based out of houston or stafford
--      a) Use OR clause
--      b) Use IN clause as in Plocation in ('Houston', 'Stafford')

-- 10. Display the names of the project that are neither based out of houston nor out of stafford
--      a) Use AND/OR clause
--      b) use NOT IN clause as in Plocation NOT IN ('Houston','Stafford')


-- 11. Display the ssn and fully concatenated name of all employees
-- 	Use CONCAT function as in CONCAT(fname, ' ', minit, ' ', lname)


-- 12. Display the employee details who does not have supervisor
-- 	Use IS NULL as in super_ssn IS NULL


-- 13. Display the ssn of employees sorted by their salary in ascending mode
-- 	Use ORDER by SALARY


-- 14. Sort the works_on table based on Pno and Hours



-- 15. Display the average project hours 




-- 16. Display the number of employees who do not have a manager




-- 17. What is the average salary of employees who do not have a manager




-- 18. What is the highest salary of female employees



-- 19. What is the least salary of male employees



-- 20. Display the number of employees in each department












-- 21. Display the average salary of employees (department-wise and gender-wise)
-- 	GROUP BY Dno, Sex



-- 22. Display the number of male employees in each department

-- 23. Display the average, minimum, maximum hours spent in each project



-- 24. Display the year-wise count of employees based on their year of birth


-- 25. Dipslay the number of projects each employee is working on

-- 26. Display the Dno of those departments that has at least 3 employees





-- 27. Among the people who draw at least 30000 salary, what is the department-wise average?


-- 27b. Instead of dno, display dname

-- 28. Display the fname of employees working in the Research department


-- 29. Display the fname and salary of employees whose salary is more than the average salary of all the employees


-- 30. Which project(s) have the least number of employees?


-- 31. Display the fname of those employees who work for at least 20 hours

-- 32. What is the average salary of those employees who have at least one
--     dependent

-- JOIN Examples


-- 33. Display the ssn, lname and the name of the department of all the employees



-- 34. Display the ssn, lname, name of project of all the employees






-- 35a. Display the ssn, their department, the project they work on and
--     the name of the department which runs that project
-- 	Hint: Needs a 5 table join
-- 	Output heading: ssn, emp-dept-name, pname, proj-dept-no


-- 35b. Display the deptname, the project the department runs
-- 	Output heading: dept-name, pname



-- SOME COMPLICATED SQL Queries for Self-Study

-- 36. What is the name of the department that has least number of 
--     employees?

-- select dname 
-- from employee e, department d 
-- where e.dno=d.dnumber 
-- group by dno having count(ssn) =
--     (select min(mycount) 
--      from (select count(ssn) as mycount 
--            from employee
--            group by dno
--           ) mytable
--     );

-- 37. What is the name of the department whose employees have the highest
--     average salary?

-- 38. Display the fname of the employee along with the fname of the manager
-- 	select e.fname 'EmpName', m.fname 'MgrName'
-- 	from employee e, employee m
-- 	where e.super_ssn = m.ssn;

-- 39. Which employees work on projects belonging to departments other
--     than departments they belong to
-- 	Output: ssn, pname, emp-dept-name, proj-dept-name

-- select e.ssn, pname, ed.dname 'emp-dept-name', pd.dname 'project-dept-name' 
-- from employee e,  works_on w,  project p,  department ed,  department pd 
-- where e.ssn = w.essn 
-- 	and w.pno = p.pnumber 
-- 	and e.dno = ed.dnumber 
-- 	and p.dnum = pd.dnumber 
-- 	and e.dno <> p.dnum;
-- ==============================================

-- LEFT OUTER JOIN

-- Inner join between employee and dependent

-- Left Outer join between employee and dependent

-- Right out joint between dependent and employee
