-- SELECT
--     ROUND(
--         SUM(
--             EXISTS (
--                 SELECT 1
--                 FROM Activity AS a2
--                 WHERE a2.player_id = a1.player_id
--                   AND DATEDIFF(a2.event_date, a1.first_login) = 1
--             )
--         ) / COUNT(*),
--         2
--     ) AS fraction
-- FROM (
--     SELECT player_id, MIN(event_date) AS first_login
--     FROM Activity
--     GROUP BY player_id
-- ) AS a1;


select
round(
    sum(
        exists(
            select 1 
            from Activity as a1 
            where a1.player_id=a2.player_id 
            and datediff(a1.event_date,a2.first_day)=1
        )
    )/count(*),
    2
) as fraction
from (
    select player_id,min(event_date) as first_day
    from Activity
    group by player_id
) as a2
