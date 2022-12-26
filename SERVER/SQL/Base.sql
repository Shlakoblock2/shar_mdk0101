

CREATE TABLE if not EXISTS product(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR,
discription VARCHAR,
price INTEGER);

CREATE TABLE if not EXISTS Cart(
id INTEGER PRIMARY KEY AUTOINCREMENT,
amount INTEGER,
productID INTEGER not null,
foreign key(productID)references product(id));

CREATE TABLE if not EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
phone VARCHAR,
name VARCHAR,
 surname VARCHAR,
 cartID INTEGER not null,
 foreign key(cartID)references Cart(id));

CREATE TABLE if not EXISTS personal(
id INTEGER PRIMARY KEY AUTOINCREMENT,
phone VARCHAR,
name VARCHAR,
surname VARCHAR,
powerlevel VARCHAR);

INSERT INTO product(name,discription,price)
VALUES ("electro gitara","gitara",1900);
INSERT INTO product(name,discription,price)
VALUES ("electro gitara1","gitara1",2000);
INSERT INTO Cart(amount,productID)
VALUES (1,1);
INSERT INTO Cart(amount,productID)
VALUES (1,2);  
 INSERT INTO users(phone, name, surname,cartID)
VALUES ('+78965487','SASHA','IVANOV',1);
INSERT INTO users(phone, name, surname,cartID)
 VALUES ('+78968527','NIKITA','VISOTCKYI',2);

 INSERT INTO personal(phone, name, surname,powerlevel)
VALUES ('+78965487','EGOR','GABRIELEV',1);
INSERT INTO personal(phone, name, surname,powerlevel)
 VALUES ('+78968527','NEYMAR','KALMAR',2);
