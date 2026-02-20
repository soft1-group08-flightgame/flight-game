import random
import mariadb

connection = mariadb.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    # password="PASSWORD",
    database="flight_game",
    autocommit=True
)

MONTHS = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

# Each tournament:
# ("Tournament Name", points_if_win, money_if_win, airport_ident)
#
# airport_ident = ICAO code
TOURNAMENTS = [
    ("Australian Open (Melbourne)", 700, 10000, "YMML"),  # Melbourne
    ("Dubai Open", 300, 5000, "OMDB"),                    # Dubai
    ("Indian Wells", 500, 7000, "KPSP"),                  # Palm Springs (near Indian Wells)
    ("Monte Carlo", 500, 7000, "LFMN"),                   # Nice (near Monaco)
    ("Rome Open", 500, 7000, "LIRF"),                     # Rome Fiumicino
    ("Roland Garros (Paris)", 700, 10000, "LFPG"),        # Paris CDG
    ("Wimbledon (London)", 700, 10000, "EGLL"),           # London Heathrow
    ("Cincinnati", 500, 7000, "KCVG"),                    # Cincinnati/Northern Kentucky
    ("US Open (New York)", 700, 10000, "KJFK"),           # New York JFK
    ("Shanghai", 500, 7000, "ZSPD"),                      # Shanghai Pudong
    ("Paris Masters", 500, 7000, "LFPG"),                 # Paris CDG
    ("Season Final (London)", 600, 8000, "EGLL"),         # simplified
]

START_MONEY = 3000
FLIGHT_COST = 100
ENTRY_FEE = 50

START_SKILL = 20
WIN_THRESHOLD = ??????? # random(1..100) + skill >= ??????  <------# to still set in common according

#I started to create the python file. RODRI in case make every necessary change