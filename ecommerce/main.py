import products

# Usage example: recommending products related to the "fashion" category
target_category = "fashion"
recommendations =products.recommend_products_by_category(target_category)
print(f"Products related to category '{target_category}':")
for product in recommendations:
     print(f"- {product['name']}")