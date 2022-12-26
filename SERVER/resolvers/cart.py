from SERVER.SQL.models import Cart
from SERVER.SQL.dbmanager import DbManager

dbmanager = DbManager(base_path='SERVER/SQL/shop.db')

def create(_Cart: Cart) -> int:
    new_id = dbmanager.execute(
        query="insert into Cart(productId, amount) values(?, ?)",
        args=(_Cart.productId, _Cart.amount)
    )
    return new_id

def get(Cart_id: int) -> Cart | None:
    res = dbmanager.execute(
        query='select * from Cart where id=(?)',
        args=(Cart_id,)
    )

    return None if not res else Cart(
        id=res[0],
        productId=res[1],
        amount=res[2]
    )
def get_all() -> list[Cart]:
    Cart_list = dbmanager.execute(query= "select * from Cart",many=True)
    res = []

    if Cart_list:
        for Cart in Cart_list:
            res.append(Cart(
                id=Cart[0],
                productId=Cart[1],
                amount=Cart[2]
            ))

    return res

def remove(Cart_id: int) -> None:
    return dbmanager.execute('delete from Cart where id=(?)', args=(Cart_id,))

def update(Cart_id: int, new_data: Cart) -> None:
    return dbmanager.execute(
        query='update Cart set (productId, amount) = (?, ?) where id=(?)',
        args=(new_data.productId, new_data. amount, Cart_id))

