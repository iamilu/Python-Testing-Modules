import pytest

class InsufficientException(Exception):
    pass
    
class MobileInventory:

    def __init__(self, inventory = None):
        self.balance_inventory = inventory
        print(self.balance_inventory)

        if not isinstance(self.balance_inventory, dict):
            raise TypeError('Input inventory must be a dictionary')
        
        for item in self.balance_inventory.keys():
            if not isinstance(item, str):
                raise ValueError('Mobile model name must be a string')
            
        for item in self.balance_inventory.values():
            if not isinstance(item, int) or item < 0:
                raise ValueError('No. of mobiles must be a positive integer')

    def add_stock(self, new_stock=None):
        
        if not isinstance(new_stock, dict):
            raise TypeError('Input stock must be a dictionary')
        
        for item in new_stock.keys():
            if not isinstance(item, str):
                raise ValueError('Mobile model name must be a string')
            
        for item in new_stock.values():
            if not isinstance(item, int) or item < 0:
                raise ValueError('No. of mobiles must be a positive integer')

    def sell_stock(self, requested_stock):

        if not isinstance(requested_stock, dict):
            raise TypeError('Requested stock must be a dictionary')
        
        for item in requested_stock.keys():
            if not isinstance(item, str):
                raise ValueError('Mobile model name must be a string')
            
        for item in requested_stock.values():
            if not isinstance(item, int) or item < 0:
                raise ValueError('No. of mobiles must be a positive integer')

        for model_item in requested_stock.keys():
            if model_item not in [item for item in self.balance_inventory.keys()]:
                raise InsufficientException('No Stock. New Model Request')
            else:
                if requested_stock.get(model_item) > self.balance_inventory.get(model_item):
                    raise InsufficientException('Insufficient Stock')

class TestingInventoryCreation:

    def test_creating_empty_inventory(self):
        c = MobileInventory(inventory = {})
        assert c.balance_inventory == {}

    def test_creating_specified_inventory(self):
        c = MobileInventory(inventory = {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
        assert c.balance_inventory == {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25}

    def test_creating_inventory_with_list(self):
        with pytest.raises(TypeError) as e:
            c = MobileInventory(inventory = ['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
        assert e.type == TypeError

    def test_creating_inventory_with_numeric_keys(self):
        with pytest.raises(ValueError) as e:
            c = MobileInventory(inventory = {1:'iPhone Model X', 2:'Xiaomi Model Y', 3:'Nokia Model Z'})
        assert e.type == ValueError

    def test_creating_inventory_with_nonnumeric_values(self):
        with pytest.raises(ValueError) as e:
            c = MobileInventory(inventory = {'iPhone Model X':'100', 'Xiaomi Model Y': '1000', 'Nokia Model Z':'25'})
        assert e.type == ValueError

    def test_creating_inventory_with_negative_value(self):
        with pytest.raises(ValueError) as e:
            c = MobileInventory(inventory = {'iPhone Model X':-45, 'Xiaomi Model Y': 200, 'Nokia Model Z':25})
        assert e.type == ValueError

class TestInventoryAddStock:
    
    @classmethod
    def setup_class(cls):
        c = MobileInventory(inventory = {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
        assert c.balance_inventory == {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25}
    def test_add_new_stock_as_dict(self):
        c = MobileInventory(inventory = {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
        c.add_stock({'iPhone Model X':50, 'Xiaomi Model Y': 2000, 'Nokia Model A':10})
        c.balance_inventory = {'iPhone Model X':150, 'Xiaomi Model Y': 3000, 'Nokia Model Z':25, 'Nokia Model A':10}
    def test_add_new_stock_as_list(self):
        c = MobileInventory(inventory = {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
        with pytest.raises(TypeError) as e:
            c.add_stock(new_stock = ['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
        assert e.type == TypeError
    def test_add_new_stock_with_numeric_keys(self):
        c = MobileInventory(inventory = {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
        with pytest.raises(ValueError) as e:
            c.add_stock(new_stock = {1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'})
        assert e.type == ValueError
    def test_add_new_stock_with_nonnumeric_values(self):
        c = MobileInventory(inventory = {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
        with pytest.raises(ValueError) as e:
            c.add_stock(new_stock = {'iPhone Model A':'50', 'Xiaomi Model B':'2000', 'Nokia Model C':'25'})
        assert e.type == ValueError
    def test_add_new_stock_with_float_values(self):
        c = MobileInventory(inventory = {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
        with pytest.raises(ValueError) as e:
            c.add_stock(new_stock = {'iPhone Model A':50.5, 'Xiaomi Model B':2000.3, 'Nokia Model C':25})
        assert e.type == ValueError

class TestInventorySellStock:
    
    @classmethod
    def setup_class(cls):
        c = MobileInventory(inventory =  {'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1})
        assert c.balance_inventory == {'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1}
    def test_sell_stock_as_dict(self):
        c = MobileInventory(inventory =  {'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1})
        c.sell_stock({'iPhone Model A':2, 'Xiaomi Model B':20, 'Sony Model D':1})
        c.balance_inventory = {'iPhone Model A':48, 'Xiaomi Model B': 1980, 'Nokia Model C':10, 'Sony Model D':0}
    def test_sell_stock_as_list(self):
        c = MobileInventory(inventory =  {'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1})
        with pytest.raises(TypeError) as e:
             c.sell_stock(['iPhone Model A', 'Xiaomi Model B', 'Nokia Model C'])
        assert e.type == TypeError
    def test_sell_stock_with_numeric_keys(self):
        c = MobileInventory(inventory =  {'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1})
        with pytest.raises(ValueError) as e:
            c.sell_stock({1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'})
        assert e.type == ValueError
    def test_sell_stock_with_nonnumeric_values(self):
        c = MobileInventory(inventory =  {'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1})
        with pytest.raises(ValueError) as e:
            c.sell_stock({'iPhone Model A':'2', 'Xiaomi Model B':'3', 'Nokia Model C':'4'})
        assert e.type == ValueError
    def test_sell_stock_with_float_values(self):
        c = MobileInventory(inventory =  {'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1})
        with pytest.raises(ValueError) as e:
            c.sell_stock({'iPhone Model A':2.5, 'Xiaomi Model B':3.1, 'Nokia Model C':4})
        assert e.type == ValueError
    def test_sell_stock_of_nonexisting_model(self):
        c = MobileInventory(inventory = {'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1})
        with pytest.raises(InsufficientException) as e:
            c.sell_stock({'iPhone Model A':2, 'Xiaomi Model B':5, 'Nokia Model C': 15})
        assert e.type == InsufficientException
    def test_sell_stock_of_insufficient_stock(self):
        c = MobileInventory(inventory = {'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1})
        with pytest.raises(InsufficientException) as e:
            c.sell_stock({'iPhone Model A':2, 'Xiaomi Model B':5, 'Nokia Model C': 15})
        assert e.type == InsufficientException
