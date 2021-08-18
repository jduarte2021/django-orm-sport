from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count


from . import team_maker

def index(request):
	
	context = {
		
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"orm21": Team.objects.filter(league__name="Atlantic Soccer Conference"),
		"orm22": Player.objects.filter(curr_team=Team.objects.get(location="Boston", team_name="Penguins")),
		"orm23": Player.objects.filter(curr_team__in=Team.objects.filter(league__in=(League.objects.filter(name__contains="International Collegiate Baseball Conference")))),
		"orm24": Player.objects.filter(curr_team__in=Team.objects.filter(league__in=(League.objects.filter(name__contains="American Conference of Amateur Football")))) & Player.objects.filter(last_name ="Lopez"),
		"orm25": Player.objects.filter(curr_team__in=Team.objects.filter(league__in=(League.objects.filter(name__contains="Football")))),
		"orm26": Team.objects.filter(curr_players__in=Player.objects.filter(first_name ="Sophia")),
		"orm27": League.objects.filter(teams__in=Team.objects.filter(curr_players__in=Player.objects.filter(first_name ="Sophia"))),
		"orm28": Player.objects.filter(last_name ="Flores").exclude(curr_team=Team.objects.get(location="Washington", team_name="Roughriders")),
		"orm29": Team.objects.filter(all_players__in=Player.objects.filter(first_name ="Samuel")),
		"orm210": Player.objects.filter(all_teams=Team.objects.get(location="Manitoba", team_name="Tiger-Cats")),
		"orm211": Player.objects.filter(all_teams=Team.objects.get(team_name="Vikings",location="Wichita")).exclude(curr_team=Team.objects.get(team_name="Vikings",location="Wichita")),
		"orm212": Team.objects.filter(all_players__in=Player.objects.filter(first_name ="Jacob",last_name="Gray")).exclude(team_name="Colts",location="Oregon"),
		"orm213": Player.objects.filter(first_name ="Joshua") & Player.objects.filter(curr_team__in=Team.objects.filter(league__in=(League.objects.filter(name__contains="International Collegiate Baseball Conference")))),
		"orm214": Team.objects.annotate(jugadores=Count('all_players')).filter(jugadores__gte = 12),
		"orm215": Player.objects.annotate(numero_teams=Count('all_teams')).order_by('numero_teams'),
		
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")