CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
Set N = N-1 ;
  RETURN (
      select Distinct(salary) from Employee 
      Order By salary desc
      limit 1 offset N

  );
END