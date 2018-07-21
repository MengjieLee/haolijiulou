from django.shortcuts import render


# 主页
def home(request):
    return render(
        request,
        'app_pages/home.html',
        {
            "title":"主页",
        }
    )


# 菜单
def market(request):
    return render(
        request,
        'app_pages/market.html',
        {
            "title":"菜单",
        }
    )


# 购物车
def cart(request):
    return render(
        request,
        'app_pages/cart.html',
        {
            "title":"购物车",
        }
    )


# 关于我
def mine(request):
    return render(
        request,
        'app_pages/mine.html',
        {
            "title":"关于我",
        }
    )
