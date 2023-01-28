#1. What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, 
#language and language percentage. Your query should arrange the result by language percentage in descending order. (1)

SELECT   countries.name ,languages.language ,languages.percentage FROM languages
JOIN countries on countries.id  = languages.country_id 
Where  languages.language='slovene'
ORDER BY languages.percentage DESC

# 2. What query would you run to display the total number of cities for each country? 
#Your query should return the name of the country and the total number of cities. Your query should arrange the result by the number of cities in descending order. (3)

SELECT countries.name as country_name , COUNT( cities.name) AS number_of_cities from cities 
JOIN COUNTRIES ON COUNTRIES.ID = CITIES.COUNTRY_ID 
GROUP BY countries.name 
Order by number_of_cities DESC

# 3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order. (1)

SELECT cities.name , cities.population from cities 
Join countries on countries.id = cities.country_id
where countries.name = "Mexico" and cities.population > 500000
order by cities.population DESC 

#4. What query would you run to get all languages in each country with a percentage greater than 89%? 
#Your query should arrange the result by percentage in descending order. (1)

SELECT countries.name as country_name , languages.language as language_name, languages.percentage as language_percent from languages  
LEFT  JOIN countries on countries.id  = languages.country_id 
where languages.percentage > 89
order by languages.percentage DESC 

# 5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)

SELECT countries.name  , countries.surface_area , countries.population from countries
where surface_area < 501 and population > 100000 

# 6. What query would you run to get countries with only
# Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years? (1)

SELECT countries.name  , countries.government_form , countries.capital , countries.life_expectancy from countries
where countries.government_form = "Constitutional Monarchy" and countries.capital > 200 and countries.life_expectancy > 75 

#7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000?
# The query should return the Country Name, City Name, District and Population. (2)

SELECT countries.name AS country_name, cities.name AS city_name, cities.district, cities.population from cities
JOIN countries ON countries.id = cities.country_id 
where countries.name = 'Argentina' and cities.district = 'Buenos Aires' and cities.population >500000 ;

#8. What query would you run to summarize the number of countries in each region? The query should display the name of the region and the number of countries. Also,
#the query should arrange the result by the number of countries in descending order. (2)
 
SELECT countries.region , COUNT(countries.name) as Number_Of_Countries from countries 
group by countries.region
order by Number_Of_Countries DESC 