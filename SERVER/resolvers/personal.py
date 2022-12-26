from SERVER.SQL.models import Personal
from SERVER.SQL.dbmanager import DbManager

dbmanager = DbManager(base_path='SERVER/SQL/shop.db')

def create(_personal: Personal) -> int:
    new_id = dbmanager.execute(
        query="insert into Personal(name, surname, power_level) values(?, ?, ?)",
        args=(_personal.name, _personal.surname, _personal.power_level)
    )
    return new_id

def get(personal_id: int) -> Personal | None:
    res = dbmanager.execute(
        query='select * from Personal where id=(?)',
        args=(personal_id,)
    )

    return None if not res else Personal(
        id=res[0],
        name=res[1],
        surname=res[2],
        power_level=res[3]
    )
def get_all() -> list[Personal]:
    personal_list = dbmanager.execute(query= "select * from Personal", many=True)
    res = []

    if personal_list:
        for personal in personal_list:
            res.append(Personal(
                id=personal[0],
                name=personal[1],
                surname=personal[2],
                power_level=personal[3]
            ))

    return res

def remove(personal_id: int) -> None:
    return dbmanager.execute('delete from Personal where id=(?)', args=(personal_id,))

def update(personal_id: int, new_data: Personal) -> None:
    return dbmanager.execute(
        query='update Personal set (name, surname, power_level) = (?, ?, ?) where id=(?)',
        args=(new_data.name, new_data.surname, new_data.power_level,personal_id))

