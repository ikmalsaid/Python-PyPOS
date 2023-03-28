import data_manager as dm

# Add a new product
dm.add_product('Product 1', 10.99, 100)

# Add multiple products
products_data = [('Product 2', 20.99, 50), ('Product 3', 30.99, 75)]
dm.batch_add_products(products_data)

# Retrieve all products
all_products = dm.get_all_products()
print(all_products)

# Edit a product
dm.edit_product(1, 'Updated Product', 15.99, 200)

# Delete a product
dm.delete_product(2)
