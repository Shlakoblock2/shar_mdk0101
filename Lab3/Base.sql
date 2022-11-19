CREATE TABLE if not EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
phone VARCHAR,
name VARCHAR,
 surname VARCHAR,
cartID VARCHAR);

 INSERT INTO users(phone, name, surname, cartID)
VALUES ('+78965487','SASHA','IVANOV','ELECTRO GITARA');
INSERT INTO users(phone, name, surname, cartID)
 VALUES ('+78968527','NIKITA','VISOTCKYI','ELECTRO GITARA');
INSERT INTO users(phone, name, surname, cartID)
VALUES ('+78967777','MISHA','MNATSAKANYAN','GITARA');
INSERT INTO users(phone, name, surname, cartID)
VALUES ('+789654485','KAREN','IVANOV','PIANINO');
INSERT INTO users(phone, name, surname, cartID)
VALUES ('+7896045685','SERGEY','IVANOV','FGORTEPANO');
INSERT INTO users(phone, name, surname, cartID)
VALUES ('+7896045685','SERGEY','KAZARYAN','SCRIPKA');
INSERT INTO users(phone, name, surname, cartID)
VALUES ('+7888888888','VLADIMER','KAZARYAN','SCRIPKA');