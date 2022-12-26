from SERVER.SQL.models import Product
from SERVER.SQL.dbmanager import DbManager

dbmanager = DbManager(base_path='SERVER/SQL/shop.db')

def create(_Product: Product) -> int:
    new_id = dbmanager.execute(
        query="insert into Product(name,discription,price) values(?,?,?)",
        args=(_Product.name,_Product.discription,_Product.price)
    )
    return new_id

def get(Product_id: int) -> Product | None:
    res = dbmanager.execute(
        query='select * from Product where id=(?)',
        args=(Product_id,)
    )

    return None if not res else Product(
        id=res[0],
        name=res[1],
        discription=res[2],
        price=res[3]

    )
def get_all() -> list[Product]:
    Product_list = dbmanager.execute(query= "select * from Product",many=True)
    res = []

    if Product_list:
        for Product in Product_list:
            res.append(Product(
                id=Product[0],
                name=Product[1],
                discription=Product[2],
                price=Product[3]
            ))

    return res

def remove(Product_id: int) -> None:
    return dbmanager.execute('delete from Product where id=(?)', args=(Product_id,))

def update(Product_id: int, new_data: Product) -> None:
    return dbmanager.execute(
        query='update Product set (name,discription,price) = (?,?,?) where id=(?)',
        args=(new_data.name,new_data.discription,new_data.price, Product_id))

