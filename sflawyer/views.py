from django.shortcuts import render
from models import M_Book,M_News,M_Paper,M_Human

# Create your views here.

def home(request):
    latest_news_list = M_News.objects.order_by('-pub_date')
    if len(latest_news_list) > 5:
        latest_news_list = latest_news_list[:5]

    latest_human_list = M_Human.objects.order_by('-pub_date')
    if len(latest_human_list) > 5:
        latest_news_list = latest_human_list[:5]

    latest_paper_list = M_Paper.objects.order_by('-paper_pub_date')
    if len(latest_paper_list) > 5:
        latest_paper_list = latest_paper_list[:5]
    return render(request, 'sflawyer/index.html',{'latest_news_list':latest_news_list,'latest_paper_list':latest_paper_list,
                                                  'latest_human_list': latest_human_list})

def about(request, abouttype):
    if abouttype == 'overall':
        return render(request, 'sflawyer/about.html')
    elif abouttype == 'theary':
        return render(request, 'sflawyer/about_thy.html')
    else:
        return render(request, 'sflawyer/about_cmp.html')

def team(request):
    return render(request, 'sflawyer/team.html')

def part(request):
    return render(request, 'sflawyer/partner.html')

def jion(request):
    return render(request, 'sflawyer/jion.html')

def book(request,book_index):
    if not book_index:
        latest_book_list = M_Book.objects.order_by('-pub_date')
        return render(request, 'sflawyer/book.html',{'latest_book_list':latest_book_list})
    else:
        book_instance = M_Book.objects.get(pk=book_index)
        return render(request, 'sflawyer/book_content.html',{'book_instance': book_instance})

def news(request,news_index):
    if not news_index:
        latest_news_list = M_News.objects.order_by('-pub_date')
        return render(request, 'sflawyer/news.html',{'latest_news_list':latest_news_list})
    else:
        news_instance = M_News.objects.get(pk=news_index)
        return render(request, 'sflawyer/news_content.html',{'news_instance': news_instance})

def paper(request):
        latest_paper_list = M_Paper.objects.order_by('-paper_pub_date')
        return render(request, 'sflawyer/paper.html',{'latest_paper_list':latest_paper_list})

def human(request,human_index):
    if not human_index:
        latest_human_list = M_Human.objects.order_by('-pub_date')
        return render(request, 'sflawyer/human.html',{'latest_human_list':latest_human_list})
    else:
        human_instance = M_Human.objects.get(pk=human_index)
        return render(request, 'sflawyer/human_content.html',{'human_instance': human_instance})

def good(request):
    return render(request, 'sflawyer/good.html')