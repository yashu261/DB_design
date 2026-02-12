# customer support
# return order
# update profile
# update password
# filter products
# payment modes
# share a product link
# upload image and find similar products
from sqlalchemy import create_engine

Base = declarative_base()

class Cart(Base):
    tablename = 'cart'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    price = Column(Integer)
    total = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(),onupdate=datetime.now())


class Wishlist(Base):
    tablename = 'wishlist'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    status = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(),onupdate=datetime.now())


class Product(Base):
    tablename = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)
    category = Column(String)
    stock = Column(Integer)
    image = Column(String)
    size = Column(String)
    color = Column(String)
    brand = Column(String)
    rating = Column(Float)
    review = Column(Integer)
    is_prime = Column(Boolean)
    taxpercent = Column(Integer)
    
class ProductReview(Base):
    tablename = 'product_review'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    review = Column(String)
    rating = Column(Float)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(),onupdate=datetime.now())
    

class User(Base):
    tablename = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    address = Column(String)
    phone = Column(String)
    isprime = Column(Boolean)
    

class Order(Base):
    tablename = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    price = Column(Integer)
    total = Column(Integer)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(),onupdate=datetime.now())
    payment_type = Column(String)
    payment_status = Column(String)

class OrderDetails(Base):
    tablename = 'order_details'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    price = Column(Integer)
    total = Column(Integer)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(),onupdate=datetime.now())