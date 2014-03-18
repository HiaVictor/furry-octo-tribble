
import xml.etree.ElementTree as ET
import main
teams = []

def get_teams():
    tree = ET.parse('data.xml')
    root = tree.getroot()
    
    for team in root.findall('team'):
        global teams
        teams.append(team.find('number').text)


def get_matches_played(team_number):
    
    tree = ET.parse('data.xml')
    root = tree.getroot()
    
    for team in root.findall('team'):
        if team.find('number').text == team_number:
            value = team.find('matches_played').text
            break
    return value

#def save_data(team_number):   
    #print main.matches_played
