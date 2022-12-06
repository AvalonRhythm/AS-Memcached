use db;

CREATE TABLE students(
	StudentID int not null AUTO_INCREMENT,
	FirstName varchar(100) NOT NULL,
	Surname varchar(100) NOT NULL,
	Age int NOT NULL,
	PRIMARY KEY (StudentID)
);

INSERT INTO students(FirstName, Surname, Age) VALUES("Hugo", "Robles", 21), ("Marek", "Robles", 17);
