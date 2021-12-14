SELECT "Software".name
FROM "Software"
WHERE "Software"."developerId" IN
	(SELECT "Developers".id
	 FROM "Developers"
	 WHERE "Developers".id IN
		(SELECT D.id
		 FROM "Developers" D
		 WHERE NOT EXISTS
	 		((SELECT "Software".name
			  FROM "Software"
		      WHERE "Software"."developerId" = Q)
		     EXCEPT
		     (SELECT "Software".name
		      FROM "Software"
		      WHERE "Software"."developerId" = D.id AND "Software"."developerId" != Q))));