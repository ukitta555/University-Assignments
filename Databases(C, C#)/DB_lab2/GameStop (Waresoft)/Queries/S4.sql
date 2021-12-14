SELECT "Countries".name
FROM "Countries"
WHERE "Countries".id IN
	(SELECT "Developers"."CountryId"
	 FROM "Developers"
     WHERE "Developers".id IN
		(SELECT "Software"."developerId"
		 FROM "Software"
		 WHERE "Software".id IN
	 		(SELECT "Purchases"."softwareId"
			 FROM "Purchases"
			 WHERE "Purchases"."customerId" IN
		 		(SELECT "Customers".id
				 FROM "Customers"
				 WHERE "Customers".name = X AND "Customers".surname = Y
				 AND "Customers".email = Z))));
