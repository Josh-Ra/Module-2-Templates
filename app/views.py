from django.shortcuts import render
from django.http.response import HttpResponse
import random
from dataclasses import dataclass

@dataclass
class Team:
    name: str
    description: str
    members: list[str]


def load_page(request):
    return render(request, "home.html")


def load_team_list(request):
    context = {
        "technologies": ["management", "procurement", "documentation", "community"]
    }
    return render(request, "team_list.html", context)




def load_team_details(request, name):
    teams = {
        "management": Team("Management", "Management is responsible for ensuring each team has what they need as far as resources go and providing a fair chores list each week.", ['Owen','Jeremiah','Nick','Ab','Abigail','Mathew']),
        "procurement": Team("Procurement", "The Procurment team is responsible for budgeting our weekly food costs and providing us the nutrition we need.", ["Big John", "Wyatt", "Blaine", "Bryce", "Adrian"]),
        "documentation": Team("Documentation", "The Documentation team is responsible for managing the schools social media websites.", ["Josh", "Jay", "Mina", "Connor", "Kaleigh", "Kaylee"]),
        "community": Team("Community", "The Community team is responsible for ensuring we all come together as a community and have fun here at BaseCamp.",['Jordan','Joby','Aj','Micah','Caleb'])
    }
    
    if name.lower() in teams.keys():
        return render(request, "team_details.html", context={"Team":teams[name.lower()]})

   

