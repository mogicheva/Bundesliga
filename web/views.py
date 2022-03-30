from django.core.paginator import Paginator
from django.shortcuts import render

from web.source import Bundesliga


def show_index(request):
    upcoming = Bundesliga().bundesliga_weekend()
    final = []
    first = upcoming[0]
    final.append(first)

    context = {
        'second': final,

    }
    return render(request, 'index.html', context)


def show_table(request):
    ranking = Bundesliga().bundesliga_table()
    context = {
        'ranking': ranking,
    }
    return render(request, 'table.html', context)


def show_weekend(request):
    upcoming = Bundesliga().bundesliga_weekend()
    context = {
        'upcoming': upcoming,
    }
    return render(request, 'weekend.html', context)


def show_upcoming(request):
    upcoming = Bundesliga().bundesliga_all_upcoming()

    upcoming_paginator = Paginator(upcoming, 10)
    page_num = request.GET.get('page')
    page = upcoming_paginator.get_page(page_num)
    context = {
        'upcoming': upcoming_paginator.count,
        'page': page,
    }

    return render(request, 'upcoming.html', context)


def show_finished(request):
    season_matches = Bundesliga().bundesliga_season()
    upcoming_paginator = Paginator(season_matches, 10)
    page_num = request.GET.get('page')
    page = upcoming_paginator.get_page(page_num)
    context = {
        'season_matches': upcoming_paginator.count,
        'page': page,
    }
    return render(request, 'finished.html', context)
