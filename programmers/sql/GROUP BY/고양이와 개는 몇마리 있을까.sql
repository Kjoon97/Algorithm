select ANIMAL_TYPE, COUNT(*) AS COUNT
        from ANIMAL_INS
        group by ANIMAL_TYPE
        ORDER BY ANIMAL_TYPE;