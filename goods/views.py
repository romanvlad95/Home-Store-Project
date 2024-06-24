from django.shortcuts import render


def catalogue(request):
    context = {
        'title': 'Home - Catalogue',
        'goods': [
            {
                'image': 'deps/images/goods/set of tea table and three chairs.jpg',
                'name': 'Tea Table and Three Chairs',
                'description': 'A set of three chairs and a designer table for the living room.',
                'price': 150.00
            },
            {
                'image': 'deps/images/goods/set of tea table and two chairs.jpg',
                'name': 'Tea Table and Two Chairs',
                'description': 'A minimalist set of a table and two chairs.',
                'price': 93.00
            },
            {
                'image': 'deps/images/goods/double bed.jpg',
                'name': 'Double Bed',
                'description': 'A double bed with a headboard, very orthopedic.',
                'price': 670.00
            },
            {
                'image': 'deps/images/goods/kitchen table.jpg',
                'name': 'Kitchen Table with Sink',
                'description': 'A kitchen table with a built-in sink and chairs.',
                'price': 365.00
            },
            {
                'image': 'deps/images/goods/kitchen table 2.jpg',
                'name': 'Kitchen Table with Built-in Stove',
                'description': 'A kitchen table with a built-in stove and sink. Many shelves and very beautiful.',
                'price': 430.00
            },
            {
                'image': 'deps/images/goods/corner sofa.jpg',
                'name': 'Corner Sofa for Living Room',
                'description': 'A corner sofa that converts into a double bed, perfect for the living room and hosting guests!',
                'price': 610.00
            },
            {
                'image': 'deps/images/goods/bedside table.jpg',
                'name': 'Bedside Table',
                'description': 'A bedside table with two drawers (plant not included).',
                'price': 55.00
            },
            {
                'image': 'deps/images/goods/sofa.jpg',
                'name': 'Ordinary Sofa',
                'description': 'A regular sofa, nothing remarkable to describe.',
                'price': 190.00
            },
            {
                'image': 'deps/images/goods/office chair.jpg',
                'name': 'Office Chair',
                'description': 'Product description about how great it is, but it\'s just a chair, what else is there to say...',
                'price': 30.00
            },
            {
                'image': 'deps/images/goods/plants.jpg',
                'name': 'Plant',
                'description': 'A plant to decorate your interior, bringing freshness and tranquility to the environment.',
                'price': 10.00
            },
            {
                'image': 'deps/images/goods/flower.jpg',
                'name': 'Stylized Flower',
                'description': 'A designer flower (possibly artificial) for interior decoration.',
                'price': 15.00
            },
            {
                'image': 'deps/images/goods/strange table.jpg',
                'name': 'Strange Bedside Table',
                'description': 'A table, quite strange in appearance, but suitable for placing next to the bed.',
                'price': 25.00
            }
        ]
    }
    return render(request, 'goods/catalogue.html', context)


def product(request):
    return render(request, 'goods/product.html')
