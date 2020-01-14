#Exporting Tables using wizard

CREATE database geyserdb;
USE geyserdb;
CREATE table geyser (
time INT NOT NULL PRIMARY KEY ,
eruption FLOAT NOT NULL,
inter INT NOT NULL,
CATEGORY INT NOT NULL
);

INSERT INTO geyser VALUE
(1, 8.2, 11,4),
(745, 6.4, 10 ,5)

SELECT * FROM geyser

###Now go the bottom of the bottom left of your screen below "Schemas" 
###click on the arrow pointing down right next to the name of your database.
###now click on the arrow next to "Tables"
###Now right click on the name of your database and go to "Table Data Export Wizard"
###The instructions to export a table are pretty straightfoward.
###Email us if you have quesitons.




#Importing Tables using Wizard
###Same thing as last time, this time using "Table Data Import Wizard"
###Just hit the browse button and click on your dataset
### Create a new table, you can create a new database if you want to put it in.
###One little trick to this when you hit the window titled "COnfigure import Settings"...
### Uncheck the blank row below "Source Column", it can sometimes cause unwanted errors.