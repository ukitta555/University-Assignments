SELECT MAX("Software".price)
FROM "Software"
WHERE "Software"."developerId" IN
	(SELECT "Developers".id
	 FROM "Developers"
	 WHERE "Developers".name = P);