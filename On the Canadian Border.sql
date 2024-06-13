--Your Code Here
--SELECT name,country FROM travelers
--WHERE country != 'Canada' AND country != 'Mexico' AND country != 'USA'
--ORDER BY country ASC;

Select name,country from travelers where country not in ('Canada','Mexico','USA')