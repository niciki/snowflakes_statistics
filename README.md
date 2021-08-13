# Snowflakes and statistics
The program generates arbitrary coordinates on the canvas, the radius of the snowflake. Then a check is made for the free space that this snowflake will occupy after drawing. If the check is successful, then drawing is performed, and then the generation of new coordinates, otherwise the program will regenerate the coordinates 3000 times, hoping that it will find those that satisfy the test for emptiness (the number of attempts is in the `tests` variable). If no free space was found, then one of the snowflakes drawn on the canvas is deleted. After drawing the specified number of snowflakes (the value of the variable `number_of_snowflakes`), drawing stops, using the matplotlib library, a graph of the dependence of drawing the i-th snowflake on the number of necessary coordinates and radius regeneration is built. 
<br/>
###Image of snowflakes on canvas:###
![image](https://user-images.githubusercontent.com/71276784/129423809-b2134046-87d3-4c1b-9cc7-762c64baeee8.png)
<br/>
###Dependence of the number of attempts on the number of required generations:###
![image](https://user-images.githubusercontent.com/71276784/129423797-dbec29b0-6ade-40b3-b3f8-49cf4ccf79cd.png)
