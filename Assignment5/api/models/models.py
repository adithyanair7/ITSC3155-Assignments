from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from api.dependencies.database import Base

class Sandwich(Base):
    __tablename__ = "sandwiches"
    id = Column(Integer, primary_key=True, index=True)
    sandwich_name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    recipes = relationship("Recipe", back_populates="sandwich")
    order_details = relationship("OrderDetail", back_populates="sandwich")

class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True, index=True)
    item = Column(String(255), nullable=False)
    amount = Column(Integer, nullable=False)
    recipes = relationship("Recipe", back_populates="resource")

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))
    amount = Column(Integer, nullable=False)
    sandwich = relationship("Sandwich", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    order_details = relationship("OrderDetail", back_populates="order")

class OrderDetail(Base):
    __tablename__ = "order_details"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    amount = Column(Integer, nullable=False)
    order = relationship("Order", back_populates="order_details")
    sandwich = relationship("Sandwich", back_populates="order_details")
