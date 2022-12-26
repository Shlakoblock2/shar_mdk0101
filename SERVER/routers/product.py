from fastapi import APIRouter
from SERVER.SQL.models import Product
from SERVER.resolvers import product

router = APIRouter(prefix='/Product', tags=['Product'])

@router.post('/create')
def create(_Product: Product) -> int:
    new_id = Product.create(_Product)
    return f'{{code: 201, id: {new_id}}}'

@router.get('/get/{product_Id}')
def get(product_Id: int) -> Product | None:
    return Product.get(product_Id)

@router.get('/')
def get_all() -> list[Product] | None:
    return Product.get_all()

@router.get('/remove/{product_Id}')
def remove(product_Id: int) -> None:
    return Product.remove(product_Id)


@router.put("/update/{product_Id}")
def update(product_Id: int, new_data: Product):
    return Product.update(product_Id=product_Id, new_data=new_data)

