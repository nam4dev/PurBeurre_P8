from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from purbeurre_off.models import Product


# Create your views here.
def results(request):
    query = request.GET.get('query')
    product_searched = Product.objects.search(query)
    # if nothing found, product not found
    if not product_searched:
        return render(request, 'purbeurre_results/prod_not_found.html', locals())
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


def detail(request, product_id=None):
    product = Product.objects.filter(id=product_id)
    return render(request, 'purbeurre_results/detail.html', locals())
