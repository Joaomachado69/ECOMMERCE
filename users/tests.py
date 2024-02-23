from django.test import TestCase
from .models import User, Supplier, Product, PriceHistory, CustomerReview

#Unitary tests
class ModelTestCase(TestCase):
    def setUp(self):
        # Configuração inicial com alguns dados de exemplo
        self.user = User.objects.create(name='Test User', gender='Male', age=25)
        self.supplier = Supplier.objects.create(name='Supplier A')
        self.product = Product.objects.create(name='Test Product', supplier=self.supplier)
        self.price_history = PriceHistory.objects.create(product=self.product, price=50)
        self.customer_review = CustomerReview.objects.create(product=self.product, customer=self.user, rating=4)

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.gender, 'Male')
        self.assertEqual(self.user.age, 25)

    def test_supplier_creation(self):
        self.assertEqual(self.supplier.name, 'Supplier A')

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.supplier, self.supplier)

    def test_price_history_creation(self):
        self.assertEqual(self.price_history.product, self.product)
        self.assertEqual(self.price_history.price, 50)

    def test_customer_review_creation(self):
        self.assertEqual(self.customer_review.product, self.product)
        self.assertEqual(self.customer_review.customer, self.user)
        self.assertEqual(self.customer_review.rating, 4)


#Integration Tests
class ProductSupplierIntegrationTest(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name='Supplier A')

    def test_create_product_with_supplier(self):
        product = Product.objects.create(name='Test Product', supplier=self.supplier)
        self.assertEqual(product.supplier, self.supplier)

class ProductPriceHistoryIntegrationTest(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name='Supplier A')
        self.product = Product.objects.create(name='Test Product', supplier=self.supplier)

    def test_create_price_history_for_product(self):
        price_history = PriceHistory.objects.create(product=self.product, price=10.00)
        self.assertEqual(price_history.product, self.product)

class ProductCustomerReviewIntegrationTest(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name='Supplier A')
        self.product = Product.objects.create(name='Test Product', supplier=self.supplier)
        self.user = User.objects.create(name='Test User', gender='Male', age=25)

    def test_create_customer_review_for_product(self):
        review = CustomerReview.objects.create(product=self.product, customer=self.user, rating=5)
        self.assertEqual(review.product, self.product)
        self.assertEqual(review.customer, self.user)



#StressTest
class StressTest(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name='Supplier A')

    def test_create_many_products(self):
        for i in range(1000):  
            Product.objects.create(name=f'Test Product {i}', supplier=self.supplier)


