/*
a) In actor columns the information includes is actor_id, first_name,last_name and last_update. 
b) For the film columns, it has the film_id, title, description, release_year, language_id, original_language, rental_duration, rental_date, length, replacement_cost, rating, special_features and last_updates. 
c) The table that contains both actor_id and film_id is in the column of film_actor
d) The information given is easy to read as it has the rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, and last_update. Everything is given in a straight and detailed line making it easy to understand.
e) The inventory table track physical or digital copies of films available at store locations, such as inventory_id, film_id, store_id, and last_update
f) The tables that are required are rental, inventory and film. The rental table shows the exact rental_date, but it only links to an inventory_id. The inventory table connects that specific physical copy to a general film_id. The film table uses the film_id to provide the human-readable movie title. 
*/

SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory; 
SELECT film_id, title FROM film;