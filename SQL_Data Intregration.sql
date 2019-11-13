##Joining/Appending Tables

CREATE TABLE tblCountry (
CountryID INT NOT NULL PRIMARY KEY,
CountryName VARCHAR(30) NOT NULL);

INSERT INTO tblCountry VALUES
(1,"India"),
(2,"Nepal")


CREATE TABLE tblState (
StateID INT NOT NULL PRIMARY KEY,
CountryID INT  ,
StateName VARCHAR(30) NOT NULL);

INSERT INTO tblState VALUES 
(1,1,"Maharastra"),
(2,1 ,"Punjab"),
(3,2,"Kathmandu"),
(4,NULL,"California")

SELECT * FROM tblCountry
SELECT * FROM tblState

###Inner Join (Appending) [Main Application]
###Joining columns from a table onto a different table using a specific column (usually a key)


SELECT * FROM tblCountry
		INNER JOIN tblState
        ON tblCountry.CountryID=tblState.CountryID
        
###Left Join 
###Joining the tables in terms of the table being joined

SELECT * FROM tblCountry
		LEFT JOIN tblState
        ON tblCountry.CountryID=tblState.CountryID
        
###Right Join 
###Joining the tables in terms of the table trying to join


SELECT * FROM tblCountry
		RIGHT JOIN tblState
        ON tblCountry.CountryID=tblState.CountryID
        
###Full Outer Join
###Joining in terms of both tables

SELECT * FROM tblCountry
LEFT JOIN tblState ON tblCountry.CountryID = tblState.StateID
UNION
SELECT * FROM tblCountry
RIGHT JOIN tblState ON tblCountry.CountryID= tblState.StateID
        
##Enriching Aggegate Measures

CREATE TABLE Table4 (
ID INT  NOT NULL,
Value1 INT NOT NULL,
Value2 INT NOT NULL);

INSERT INTO Table4 VALUES
(1, 1, 2),
(1, 2, 2),
(2, 3, 4),
(2, 4, 5)

SELECT * FROM Table4 

##Sum Values by ID
SELECT  ID, SUM(VALUE1), SUM(VALUE2)
FROM    tableName
GROUP   BY ID

##Add columns of Value1 and Value2
SELECT  ID, VALUE1 + VALUE2
FROM    TableName


##Now group by a ID
SELECT  ID, SUM(VALUE1 + VALUE2)
FROM    tableName
GROUP   BY ID

###Same could be done with division (/), multiplication (*), and subtraction (-)
###Many different functions you could use (list was in the video).