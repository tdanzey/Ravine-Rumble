# call package to autheticate
from yahoo_oauth import OAuth2

#authenticate session
oauth = OAuth2(None, None, from_file='yahoo_api_credentials.json')

#query data
response = oauth.session.get('https://fantasysports.yahooapis.com/fantasy/v2/league/223.l.632756')
