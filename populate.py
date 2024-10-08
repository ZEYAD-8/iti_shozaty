from products.models import Shoe
from categories.models import category


categories = [
    "Sneakers", "Boots", "Sandals", "Loafers", "Heels", "Flats", "Sports Shoes", "Formal Shoes"
]
category_objects = [category(name=cat_name, description=f"{cat_name} description") for cat_name in categories]
category.objects.bulk_create(category_objects)


shoes = [
    Shoe(
        name=f"Shoe Model {i}",
        description=f"Description for shoe model {i}",
        price=i * 10 + 50,  
        stock=100 - i, 
        image=f"shoe_images/shoe_{i}.png",
        category=category.objects.order_by("?").first()  
    )
    for i in range(1, 31)
]

Shoe.objects.bulk_create(shoes)

print("Database populated with 30 shoes and 8 categories.")