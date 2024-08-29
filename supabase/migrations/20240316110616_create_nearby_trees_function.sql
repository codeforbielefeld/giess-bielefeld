CREATE OR REPLACE FUNCTION nearby_trees(lat float, long float)
    RETURNS TABLE (uuid public.trees.uuid%TYPE, tree_type_german public.trees.tree_type_german%TYPE, lat float, long float, dist_meters float)
    LANGUAGE sql
AS $$
    SELECT uuid, tree_type_german, ST_Y(geocoordinates::geometry) AS lat, ST_X(geocoordinates::geometry) as long, ST_Distance(geocoordinates, st_point(long, lat)::geography) AS dist_meters
    FROM public.trees
    ORDER BY geocoordinates <-> st_point(long, lat)::geography;
$$;