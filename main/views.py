from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, ProductCartItem, AboutPage
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .forms import ProductCartItemForm, ProductUpdateForm
from django.urls.exceptions import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.forms import UserReviewForm
from users.models import UserReview


def index_main(req):
    review = UserReviewForm()
    if req.method == 'POST':
        review = UserReviewForm(req.POST)
        if review.is_valid() and req.user.is_authenticated:
            review.instance.user = req.user
            messages.success(req, 'Thank you for providing a feedback')
            review.save()
            return redirect('main_home')
        elif not req.user.is_authenticated:
            messages.warning(req, 'You need to log in for this action!')
            return redirect('main_home')
        elif review.errors.items():
            for fields, error in review.errors.items():
                messages.warning(req, f'{error}')
    about = AboutPage.objects.order_by('-changed_at').first()
    clients = UserReview.objects.filter(approved=True).order_by('-sent_at')[:8]
    services = Category.objects.order_by('-updated_at')[:4]
    furnitures = Product.objects.filter(is_active=True).order_by('-updated_at')[:2]
    data = {
        'services': services,
        'furnitures': furnitures,
        'review': review,
        'clients': clients,
        'about': about
    }
    return render(req, 'main/index_main.html', data)


def index_services(req):
    services = Category.objects.order_by('-updated_at')
    return render(req, 'main/index_services.html', {'services': services})


def index_about(req):
    about = AboutPage.objects.order_by('-changed_at').first()
    return render(req, 'main/index_about.html', {'about': about})

def about_detail(req):
    about = AboutPage.objects.order_by('-changed_at').first()
    return render(req, 'main/about_detail.html', {'about': about})


class ProductList(ListView):
    model = Product
    template_name = 'main/index_shop.html'
    context_object_name = 'furnitures'
    paginate_by = 20

    def get_queryset(self):
        return Product.objects.filter(is_active=True).order_by('-updated_at')


class ProductListBycategory(ListView):
    model = Product
    template_name = 'main/products/product_list_by-category.html'
    context_object_name = 'furnitures'
    paginate_by = 20

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return Product.objects.filter(category=category, is_active=True).order_by('-updated_at')


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'main/products/product_detail.html'
    login_url = '/users/login/'



class CategoryDetail(DetailView):
    model = Category
    template_name = 'main/products/category_detail.html'
    context_object_name = 'category'


@login_required(login_url='login')
def add_to_cart(req, slug):
    product = get_object_or_404(Product, slug=slug)
    try:
        cart_item = get_object_or_404(ProductCartItem, product=product, user=req.user)
        if req.method == "POST":
            form = ProductCartItemForm(req.POST, instance=cart_item)
            if form.is_valid() and form.instance.quantity > 0 and form.instance.quantity <= product.total:
                messages.success(req, 'Product quantity has been updated in your cart!')
                form.save()
                return redirect('product_cart')
            elif form.is_valid() and form.instance.quantity <= 0:
                messages.warning(req, 'Quantity should be positive integer!')
            elif form.instance.quantity > product.total:
                messages.warning(req, f'We have only {product.total} units of product! You cannot buy more.')
    except Http404:
        if req.method == "POST":
            form = ProductCartItemForm(req.POST)
            if form.is_valid() and form.instance.quantity > 0 and form.instance.quantity <= product.total:
                messages.success(req, 'Product has been added to your cart!')
                ProductCartItem.objects.create(user=req.user, product=product, quantity=form.instance.quantity)
                return redirect('product_cart')
            elif form.is_valid() and form.instance.quantity <= 0:
                messages.warning(req, 'Quantity should be positive integer!')
            elif form.instance.quantity > product.total:
                messages.warning(req, f'We have only {product.total} units of product! You cannot buy more.')
    finally:
        cart_item = ProductCartItem.objects.filter(product=product, user=req.user).first()
        form = ProductCartItemForm(instance=cart_item)
    return render(req, 'main/products/add_to_cart.html',{'form': form})


class ProductCartList(LoginRequiredMixin, ProductList):
    model = ProductCartItem
    template_name = 'main/products/product_cart.html'
    context_object_name = 'products'
    login_url = '/users/login/'

    def get_queryset(self):
        return ProductCartItem.objects.filter(user=self.request.user).order_by('-added_at')


class ProductUpdate(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'main/staff/product_update.html'
    context_object_name = 'product'

    def form_valid(self, form):
        messages.info(self.request, 'Changes have been applied!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, error in form.errors.items():
            messages.warning(self.request, f'{error}')
        return super().form_invalid(form)

    def test_func(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return True
        return False


class ProductDelete(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'main/staff/product_delete.html'
    context_object_name = 'product'
    success_url = '/shop/'

    def test_func(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return True
        return False


class DeleteCartItem(LoginRequiredMixin, DeleteView):
    model = ProductCartItem
    template_name = 'main/products/delete_from_cart.html'
    context_object_name = 'item'
    success_url = '/product_cart/'
    login_url = '/users/login/'


class CreateReview(LoginRequiredMixin, CreateView):
    model = UserReview
    form_class = UserReviewForm
    success_url = '/contact/'
    template_name = 'main/index_contact.html'
    login_url = '/users/login/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Thank you for your feedback!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for fields, error in form.errors.items():
            messages.warning(self.request, f'{error}')
        return super().form_invalid(form)


def order_products(req):
    products = ProductCartItem.objects.filter(user=req.user).order_by('-added_at')
    number = ProductCartItem.objects.filter(user=req.user).count()
    total_price = 0
    for i in products:
        total_price += i.product.price * i.quantity
    data = {
        'products': products,
        'number': number,
        'total_price': total_price
    }
    return render(req, 'main/products/order_products.html', data)


