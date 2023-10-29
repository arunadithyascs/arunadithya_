def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices

# Example usage:
products = ["Apple", "Samsung", "Oppo", "Samsung", "Xiomi", "Apple"]
target = "Samsung"
result = linear_search_product(products, target)
print("Indices of", target, ":", result)
