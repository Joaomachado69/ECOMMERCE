products = [
     {"id": 1, "name": "T-shirt", "categories": ["clothing", "fashion"]},
     {"id": 2, "name": "Jeans", "categories": ["clothing", "fashion"]},
     {"id": 3, "name": "Sneakers", "categories": ["shoes", "sports"]},
     {"id": 4, "name": "Soccer Ball", "categories": ["sports"]}
]

# Function to recommend products by category
def recommend_products_by_category(category):
    recommendations = []
    for product in products:
        if category in product["categorias"]:
            recommendations.append(product)
    return recommendations