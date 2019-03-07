CREATE VIEW totview as 
select DATE(time) , count(*) as
totview from log 
GROUP by date(time);


CREATE VIEW errview as 
select DATE(time),count(*) as 
errview from log 
where status like '404 NOT FOUND'
GROUP by date(time) ; 



