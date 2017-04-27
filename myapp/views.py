from django.shortcuts import render

from myapp.models import Game, Player, Team, Match


def index(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, "myapp/index.html", context)

def user(request, player_id):
    player = Player.objects.get(id=player_id)
    context = {"player": player}
    return render(request, "myapp/user.html", context)

 def team(request, team_id, ladder_id):
    teams = Team.objects.get(id=team_id)
    context = {"teams": teams}
    return render(request, "myapp/team.html", context)
#
# def ladder(request, game_id):
#     games = Game.objects.get(id=game_id)
#     context = {"games": games}
#     return render(request, "myapp/ladders.html", context)
#
# def match(request, match_id):
#     matches = Match.objects.get(id=match_id)
#     context = {
#         "matches": matches
#     }
#     return render(request, "myapp/matches.html", context)
#
# def input_result(request):
#     if request.method == "GET":
#         context = {'form': MyForm()}
#         return render(request, "polls/add_question.html", context)
#
#     elif request.method == "POST":
#         form = MyForm(request.POST)
#         if form.is_valid():
#             ghg = form.cleaned_data['question_name']
#             q = Question(question_text=ghg, pub_date=timezone.now(),
#                          owner=request.user)
#             q.save()
#             messages.add_message(request, messages.SUCCESS, 'You have successfully created a poll')
#             return redirect('polls:index')
#         else:
#             messages.add_message(request, messages.WARNING, 'There was an error in your form')
#             context = {'form': form}
#             return render(request, 'polls/add_question.html', context)
#     else:
#         return render(request, "polls/oops.html")

#def results(request, match_id, team_id):
