# Write your MySQL query statement below
(
    select 
    u.name as results
    from Users as u
    join MovieRating as r
    on u.user_id=r.user_id
    group by u.user_id
    order by count(r.movie_id) desc, u.name asc
    limit 1
)
union all
(
    select title
    from Movies as m
    join MovieRating as r
    on m.movie_id=r.movie_id
    where date_format(created_at,'%Y-%m')='2020-02'
    group by m.movie_id
    order by avg(r.rating) desc, m.title asc
    limit 1
)