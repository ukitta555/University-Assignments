SELECT D.name
FROM "Developers" D
WHERE D.id IN
	(SELECT "Software"."developerId"
	 FROM "Software"
	 WHERE "Software".price > P)
AND
	(SELECT COUNT("Software"."id")
	FROM "Software"
	WHERE "Software"."developerId" = D.id) > Q;