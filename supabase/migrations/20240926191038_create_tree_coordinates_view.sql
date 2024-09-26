CREATE VIEW tree_coordinates AS
SELECT 
    uuid, 
    crown_diameter, 
    tree_type_german, 
    ST_Y(geocoordinates::geometry) AS lat, 
    ST_X(geocoordinates::geometry) AS lng
FROM 
    trees;