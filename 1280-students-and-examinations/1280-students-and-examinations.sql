# Write your MySQL query statement below
select c.student_id, c.student_name, s.subject_name, 
count(e.subject_name) as attended_exams
from Students as c
cross join Subjects as s
left join Examinations as e
on c.student_id=e.student_id and s.subject_name=e.subject_name
group by c.student_id,s.subject_name
order by c.student_id;