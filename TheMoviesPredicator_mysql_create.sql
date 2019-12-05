CREATE TABLE `movies` (
	`id` int NOT NULL AUTO_INCREMENT,
	`title` varchar(255) NOT NULL,
	`original_title` varchar(255),
	`synopsis` TEXT,
	`genre` varchar(255),
	`rating` enum NOT NULL,
	`prod_budget` int NOT NULL,
	`marketing_budget` int NOT NULL,
	`duration` int NOT NULL,
	`release_date` DATE,
	`3d` bool,
	`director` varchar(100),
	`people` varchar(255) NOT NULL,
	`produceur` varchar(255),
	`note` FLOAT NOT NULL,
	`box_office` FLOAT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `people` (
	`id` int NOT NULL AUTO_INCREMENT,
	`firstname` varchar(255) NOT NULL,
	`lastname` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `movies_people_roles` (
	`movie_id` int NOT NULL,
	`people_id` int NOT NULL,
	`role_id` int NOT NULL
);

CREATE TABLE `roles` (
	`id` int NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `movies _origins_country` (
	`movie_id` int NOT NULL,
	`country_iso2` char(2) NOT NULL
);

CREATE TABLE `compagnies` (
	`id` int NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `movies_companies_roles` (
	`movie_id` int NOT NULL AUTO_INCREMENT,
	`company_id` int NOT NULL,
	`roles_id` int NOT NULL
);

ALTER TABLE `movies_people_roles` ADD CONSTRAINT `movies_people_roles_fk0` FOREIGN KEY (`movie_id`) REFERENCES `movies`(`id`);

ALTER TABLE `movies_people_roles` ADD CONSTRAINT `movies_people_roles_fk1` FOREIGN KEY (`people_id`) REFERENCES `people`(`id`);

ALTER TABLE `movies_people_roles` ADD CONSTRAINT `movies_people_roles_fk2` FOREIGN KEY (`role_id`) REFERENCES `roles`(`id`);

ALTER TABLE `movies _origins_country` ADD CONSTRAINT `movies _origins_country_fk0` FOREIGN KEY (`movie_id`) REFERENCES `movies`(`id`);

ALTER TABLE `movies_companies_roles` ADD CONSTRAINT `movies_companies_roles_fk0` FOREIGN KEY (`movie_id`) REFERENCES `movies`(`id`);

ALTER TABLE `movies_companies_roles` ADD CONSTRAINT `movies_companies_roles_fk1` FOREIGN KEY (`company_id`) REFERENCES `compagnies`(`id`);

ALTER TABLE `movies_companies_roles` ADD CONSTRAINT `movies_companies_roles_fk2` FOREIGN KEY (`roles_id`) REFERENCES `roles`(`id`);

