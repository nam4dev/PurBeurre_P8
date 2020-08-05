from django.shortcuts import render
from purbeurre_off.models import Product


def results(request):
    """
    Shows the products found.
    """

    query = request.GET.get('query')
    substitutes, product = Product.objects.search(query)
    # if nothing found, product not found
    if not product:
        return render(
            request, 'purbeurre_results/prod_not_found.html', dict(query=query)
        )

    return render(request, 'purbeurre_results/results.html',
                  dict(product=product, substitutes=substitutes))


def detail(request, product_id=None):
    """
    Shows the detailed page of the product.
    """
    # detailed page of the product.
    product = Product.objects.get(id=product_id)
    return render(request, 'purbeurre_results/detail.html', dict(product=product))
