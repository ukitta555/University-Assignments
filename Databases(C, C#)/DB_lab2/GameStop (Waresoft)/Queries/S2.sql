SELECT "Customers".email
FROM "Customers"
WHERE "Customers".id IN
	(SELECT "Purchases"."customerId"
	 FROM "Purchases"
	 WHERE "Purchases"."softwareId" IN
	 	(SELECT "Software".id
		 FROM "Software"
		 WHERE "Software"."developerId" IN
		 	(SELECT "Developers".id
			 FROM "Developers"
			 WHERE "Developers".name = X)))
AND "Customers".name = 'Vlad';
