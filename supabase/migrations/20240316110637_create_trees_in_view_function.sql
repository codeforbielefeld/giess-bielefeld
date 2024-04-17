CREATE OR REPLACE FUNCTION trees_in_view(min_lat float, min_long float, max_lat float, max_long float)
RETURNS TABLE (id public.trees.id%TYPE, tree_type_german public.trees.tree_type_german%TYPE, lat float, long float)
LANGUAGE sql
AS $$
    SELECT id, tree_type_german, ST_Y(geocoordinates::geometry) as lat, ST_X(geocoordinates::geometry) as long
    FROM public.trees
    WHERE geocoordinates && ST_SetSRID(ST_MakeBox2D(ST_Point(min_long, min_lat), ST_Point(max_long, max_lat)), 4326)
$$;