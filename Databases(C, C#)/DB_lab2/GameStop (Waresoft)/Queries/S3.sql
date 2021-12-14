SELECT "Developers".name
	FROM "Developers"
	WHERE "Developers"."CountryId" IN
	(SELECT "Countries".id
		FROM "Countries"
		WHERE "Countries".name = K);
