select firstname, lastname, department.name
from employeedepartmenthistory
inner join person
on person.businessentityid = employeedepartmenthistory.businessentityid
inner join department
on department.departmentid  = employeedepartmenthistory.departmentid

select firstname, lastname, department.name
from employeedepartmenthistory
inner join person
on person.businessentityid = employeedepartmenthistory.businessentityid
inner join department
on department.departmentid  = employeedepartmenthistory.departmentid
where department.name = 'Engineering'

select groupname, count(groupname) 
from department 
group by groupname 

select shift.name, count(employeedepartmenthistory.shiftid) as cantidad_de_empleados 
from shift 
join employeedepartmenthistory 
on shift.shiftid = employeedepartmenthistory.shiftid
group by shift.name