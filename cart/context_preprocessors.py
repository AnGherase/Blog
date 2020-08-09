from .cart import Cart

#creating a context processor to set the current cart into the request context
def cart(request):
    return {'cart': Cart(request)}
