SELECT
    ROUND(
        SUM(
            EXISTS (
                SELECT 1
                FROM Activity AS a2
                WHERE a2.player_id = a1.player_id
                  AND DATEDIFF(a2.event_date, a1.first_login) = 1
            )
        ) / COUNT(*),
        2
    ) AS fraction
FROM (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) AS a1;
