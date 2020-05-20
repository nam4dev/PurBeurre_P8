from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from purbeurre_off.models import Product


# Create your views here.
def results(request):
    query = request.GET.get('query')
    # looking for the product
    product_searched = Product.objects.filter(name__iexact=query).first()
    # if product not found, looking for a product with a similar name
    if not product_searched:
        product_searched = Product.objects.filter(name__icontains=query).first()
    # if still nothing found, product not found
    if not product_searched:
        pass # write something to return page : product not found
    else:
        # now search substitutes
        products_list = Product.objects.filter(category_id=product_searched.category_id)
        products_list = products_list.order_by('nutriscore')
        substitutes_list = []
        for product in products_list:
            # list only products with a better nutriscore.
            if product.nutriscore == product_searched.nutriscore:
                break
            else:
                substitutes_list.append(product)

        return render(request, 'purbeurre_results/results.html', locals())


def detail(request):
    pass
