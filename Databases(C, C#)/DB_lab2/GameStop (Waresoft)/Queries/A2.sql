SELECT C.email
FROM "Customers" C
WHERE C.email != Y
AND NOT EXISTS
    ((SELECT "Purchases"."softwareId"
      FROM "Purchases"
      WHERE "Purchases"."customerId" = C.id)
     EXCEPT
     (SELECT "Purchases"."softwareId"
      FROM "Purchases"
      WHERE "Purchases"."customerId" IN
          (SELECT "Customers".id
           FROM "Customers"
           WHERE "Customers".email = Y)))
AND NOT EXISTS
    ((SELECT "Purchases"."softwareId"
      FROM "Purchases"
      WHERE "Purchases"."customerId" IN
  	      (SELECT "Customers".id
           FROM "Customers"
           WHERE "Customers".email = Y))
     EXCEPT
     (SELECT "Purchases"."softwareId"
      FROM "Purchases"
      WHERE "Purchases"."customerId" = C.id));
