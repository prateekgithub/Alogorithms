select * from employee;

select fname as "FIRST NAME",
lname as "Last Name" from employee;

select * from employee where salary >= 30000;

select * from dependent where essn=333445555;

select * from project where Plocation="Houston" or Plocation="Stafford";

select * from project where Plocation="Houston" or dnum=4;

select Dname,Year(mgr_start_date) from department;

select Ssn from employee where Address like '%HOUSTON%';

select * from employee where fname like 'j%';

select * from employee where (sex='M' and salary > 30000) or (sex='F' and salary < 30000);

select Essn from works_on where hours < 50 and hours > 25;

select Essn from works_on where hours between 25 and 50;

select pname as 'Project Name' from project where Plocation="Houston" or Plocation="Stafford";

select pname as 'Project Name' from project where Plocation in ("Houston","Stafford");

select pname as 'Project Name' from project where Plocation != "Houston" and Plocation!="Stafford";

select pname as 'Project Name' from project where Plocation not in ("Houston","Stafford");
