SELECT "Purchases".date
FROM "Purchases"
WHERE "Purchases"."softwareId" NOT IN
	(SELECT "Software".id
	 FROM "Software"
	 WHERE "Software".name = X);