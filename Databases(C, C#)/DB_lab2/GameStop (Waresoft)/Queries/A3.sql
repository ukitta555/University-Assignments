SELECT C.surname, C.email
FROM "Customers" C
WHERE C.name = Y
AND NOT EXISTS
	((SELECT "Purchases"."softwareId"
	  FROM "Purchases"
	  WHERE "Purchases"."customerId" = C.id)
	 EXCEPT
	 (SELECT "Software".id
	  FROM "Software"))
AND NOT EXISTS
	((SELECT "Software".id
	  FROM "Software")
	 EXCEPT
	 (SELECT "Purchases"."softwareId"
	  FROM "Purchases"
	  WHERE "Purchases"."customerId" = C.id));
