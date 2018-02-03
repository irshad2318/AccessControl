"select empid, lastname ,\
                        convert(date, event_time_utc) as \
                        date_, min(CONVERT(VARCHAR(8),event_time_utc,108)) as TIMEIN \
                        ,max(CONVERT(VARCHAR(8),event_time_utc,108)) as TIMEOUT ,\
                        DATEDIFF(minute,min(CONVERT(VARCHAR(8),event_time_utc,108)),\
                        max(CONVERT(VARCHAR(8),event_time_utc,108)))  as TOTAL from events join emp on  emp.id = events.empid \
                        where cardnum = ? \
                        and convert(date, event_time_utc) \
                        between convert(date, ?) and convert(date, ?)\
                        group by cardnum, empid,lastname, convert(date, event_time_utc)  \
                        order by empid, convert(date, event_time_utc) asc "