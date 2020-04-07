QUERIES 

-- Query #1
SELECT user_info.first_name, user_info.last_name, properties_info.type, properties_info.pricing_id, rental_agreement.start_date, properties_info.location, payment_info.type_of_payment, payment_info.payment_status
FROM users.guest, users.user_info, properties.properties_info, properties.rental_agreement, transactions.payment_info
WHERE rental_agreement.guest_signee_id = guest.guest_id AND guest.guest_id = user_info.account_id
ORDER BY payment_info.type_of_payment ASC, rental_agreement.start_date DESC

-- Query #2
CREATE VIEW users.GuestListView AS
SELECT guest.guest_id, user_info.account_id, user_info.first_name, user_info.last_name, user_info.email, user_info.country FROM users.user_info
JOIN users.guest ON user_info.account_id = guest.guest_id
ORDER BY guest.guest_id

-- Query #3
SELECT * FROM properties.properties_info, users.guest, properties.rental_agreement, users.user_info
WHERE properties_info.property_id = rental_agreement.property_id AND user_info.account_id = guest.guest_id
ORDER BY properties_info.pricing_id LIMIT 1  -- returns the top entry which is the lowest number since by default items are arranged in ascending order 

-- Query #4
SELECT properties_info.property_id, properties_info.type, properties_info.number_of_rooms, properties_info.location, review_info.number_of_stars
FROM properties.properties_info, properties.rental_agreement, management.review_info, users.guest
WHERE rental_agreement.guest_signee_id = guest.guest_id 
GROUP BY properties_info.property_id, review_info.number_of_stars  
ORDER BY review_info.number_of_stars

--Query #6
SELECT properties_info.property_id, properties_info.type, properties_info.number_of_rooms, properties_info.location
FROM properties.properties_info, properties.rental_agreement
WHERE rental_agreement.start_date = '1991-03-10'

--Query #7
SELECT employee_info.employee_id, employee_info.first_name, employee_info.last_name, employee_info.works_for_branch_id, branch_info.branch_name, employee_info.salary
FROM management.employee_info, management.branch_info
WHERE employee_info.salary >= 1500  --changed from 15,000 because no one makes that much money in our company!
ORDER BY employee_info.employee_id, employee_info.manages_branch_id

--Query #8   
SELECT properties_info.type, user_info.first_name, user_info.last_name,  properties_info.location, rental_agreement.pricing_id, payment_info.type_of_payment
FROM users.user_info, properties.properties_info, properties.rental_agreement, users.host, transactions.payment_info
WHERE properties_info.owner_id = host.host_id AND host.host_id = user_info.account_id   -- to specify for a specific user you would also add another AND with host_id being a specific integer

--Query #9
UPDATE users.user_info
SET phone_number = '6132495439'
FROM users.guest
WHERE user_info.account_id = guest.guest_id AND user_info.first_name = 'Jason' AND user_info.last_name = 'Wu'

--Query #10
CREATE FUNCTION FirstNameFirst(firstName char(20), lastName char(20)) RETURNS char(50) AS $$
	SELECT CONCAT (firstName, ' ', lastName) AS FullName;
	
	$$ LANGUAGE SQL;
