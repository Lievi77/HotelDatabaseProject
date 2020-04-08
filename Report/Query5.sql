--Query #5
SELECT properties_info.property_id, type, number_of_rooms, owner_id, available_date, properties_info.pricing_id, location
FROM  properties_info, rental_agreement
WHERE rental_agreement.property_id = null; --a null value in rental_agreement says it is not rented

$$ LANGUAGE SQL;
