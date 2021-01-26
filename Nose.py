import inspect
import re
import nose.tools
from nose.tools import assert_equals, assert_raises
import math
# Define class 'Circle' and its methods with proper doctests:
class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        if not isinstance(self.radius, float):
            raise TypeError('radius must be a number')
        if self.radius < 0 or self.radius > 1000:
            raise ValueError('radius must be between 0 and 1000 inclusive')

    def area(self):
        a = math.pi * self.radius * self.radius
        return round(a, 2)
               
    def circumference(self):
        c = 2 * math.pi * self.radius
        return round(c, 2)
        
class TestCircleCreation:

    def test_creating_circle_with_numeric_radius(self):
        c1 = Circle(2.5)
        assert_equals(c1.radius, 2.5)

    def test_creating_circle_with_negative_radius(self):
        with assert_raises(ValueError) as e:
            c = Circle(-2.5)
        assert_equals(str(e.exception), "radius must be between 0 and 1000 inclusive")

    def test_creating_circle_with_greaterthan_radius(self):        
        with assert_raises(ValueError) as e:
            c = Circle(1000.1)
        assert_equals(str(e.exception), "radius must be between 0 and 1000 inclusive")        

    def test_creating_circle_with_nonnumeric_radius(self):  
        with assert_raises(TypeError) as e:
            c = Circle('')
        assert_equals(str(e.exception), "radius must be a number")

class TestCircleArea:
    
    def test_circlearea_with_random_numeric_radius(self):
        c1 = Circle(2.5)
        assert_equals(c1.area(), 19.63)
        
    def test_circlearea_with_min_radius(self):
        c2 = Circle(0.0)
        assert_equals(c2.area(), 0)
        
    def test_circlearea_with_max_radius(self):
        c3 = Circle(1000.0)
        assert_equals(c3.area(), 3141592.65)

class TestCircleCircumference:
    
    def test_circlecircum_with_random_numeric_radius(self):
        c1 = Circle(2.5)
        assert_equals(c1.circumference(), 15.71)
        
    def test_circlecircum_with_min_radius(self):
        c2 = Circle(0.0)
        assert_equals(c2.circumference(), 0)
        
    def test_circlecircum_with_max_radius(self):
        c3 = Circle(1000.0)
        assert_equals(c3.circumference(), 6283.19)
 