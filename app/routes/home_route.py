from flask import Blueprint, redirect

homepage_route = Blueprint('homepage', __name__)

@homepage_route.get("/")
def home():
    ''' Return a simple text for homepage '''
    return "Welcome to my simple API for tracking personal tasks", 200

@homepage_route.get("/repo")
def repo():
    ''' Redirect to my GitHub repository '''
    return redirect("https://github.com/Vitorugz/personal_tasks_api")

@homepage_route.get("/portfolio")
def portfolio():
    ''' Redirect to my portfolio '''
    return redirect("https://vitorugz.github.io/myPortfolio/")