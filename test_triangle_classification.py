import unittest
import traingleclassification

class TestTriangleClassification(unittest.TestCase):
    # Testcases for equilateral triangle
    def test_equilateral_triangle(self):
        
        self.assertEqual(traingleclassification.classify_triangle(1, 1, 1), 'The triangle is Equilateral') 
        self.assertNotEqual(traingleclassification.classify_triangle(1, 1, 2), 'The triangle is Equilateral')
        
        #Invalid Input
        self.assertEqual(traingleclassification.classify_triangle(0, 0, 0),'Invalid lengths')
        self.assertNotEqual(traingleclassification.classify_triangle(1, 1, 1),'Invalid lengths')

        #Float
        self.assertEqual(traingleclassification.classify_triangle(1.1, 1.1, 1.1),'The triangle is Equilateral')
        self.assertNotEqual(traingleclassification.classify_triangle(1.1, 1.2, 1.1),'The triangle is Equilateral')

        

    def test_right_angled_triangle(self):
        self.assertEqual(traingleclassification.classify_triangle(3, 4, 5), 'The triangle is Right-angled')
        self.assertNotEqual(traingleclassification.classify_triangle(3, 4, 6), 'The triangle is Right-angled')

        #Invalid Input
        self.assertEqual(traingleclassification.classify_triangle(0, 0, 0),'Invalid lengths')

        #Float
        self.assertNotEqual(traingleclassification.classify_triangle(3.1, 4.1, 5.1),'The triangle is Right-angled')

    def test_isosceles_triangle(self):
        self.assertEqual(traingleclassification.classify_triangle(1, 2, 1), 'The triangle is Isosceles')
        self.assertNotEqual(traingleclassification.classify_triangle(3, 1, 4), 'The triangle is Isosceles')

        #Invalid Input
        self.assertEqual(traingleclassification.classify_triangle(0, 0, 0),'Invalid lengths')

        #Float
        self.assertEqual(traingleclassification.classify_triangle(3.1, 3.1, 5.1),'The triangle is Isosceles')
        self.assertNotEqual(traingleclassification.classify_triangle(1.1, 1.1, 1.1),'The triangle is Isosceles')

    def test_scalene_triangle(self):
        self.assertEqual(traingleclassification.classify_triangle(1, 2, 3), 'The triangle is Scalene')
        self.assertNotEqual(traingleclassification.classify_triangle(3, 1, 1), 'The triangle is Scalene')

        #Invalid Input
        self.assertEqual(traingleclassification.classify_triangle(0, 0, 0),'Invalid lengths')

        #Float
        self.assertEqual(traingleclassification.classify_triangle(3.1, 2.1, 5.1),'The triangle is Scalene')
        self.assertNotEqual(traingleclassification.classify_triangle(1.1, 1.1, 1.1),'The triangle is Scalene')


if __name__ == '__main__':
    unittest.main()
