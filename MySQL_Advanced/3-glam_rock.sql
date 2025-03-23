-- Script sorts bands in desc order of
-- life span
SELECT band_name, IFNULL(split - formed, 0) AS lifespan
FROM metal_bands
ORDER BY lifespan DESC; 