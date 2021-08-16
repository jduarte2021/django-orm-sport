from django.shortcuts import render, redirect
from .models import League, Team, Player


from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		'leagues_baseball' : League.objects.filter(name__contains="baseball"),
		'leagues_womans' : League.objects.filter(name__contains="Women"),
		'leagues_hockey' : League.objects.filter(name__contains="hockey"),
		'leagues_nofootball' : League.objects.exclude(name__contains="Football"),
		'leagues_conference' : League.objects.filter(name__contains="conference"),
		'leagues_atlantics' : League.objects.filter(name__contains="atlantic"),
		'teams_dallas' : Team.objects.filter(location__contains="dalla"),
		'teams_raptors' : Team.objects.filter(team_name__contains="raptors"),
		'teams_t' : Team.objects.filter(team_name__startswith="t"),
		'teams_alfa' : Team.objects.order_by('location'),
		'teams_alfarev' : Team.objects.order_by('-location'),
		'jcooper' : Player.objects.filter(last_name__contains="Cooper"),
		'jjoshua' : Player.objects.filter(first_name__contains="Joshua"),
		'jcooperexjosh' : Player.objects.filter(last_name__contains="Cooper").exclude(first_name__contains="Joshua"),
		'alexorwyatt' : Player.objects.filter(first_name__contains="Alex")|Player.objects.filter(first_name__contains="Wyatt")

		
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")