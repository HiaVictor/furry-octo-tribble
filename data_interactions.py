
import xml.etree.ElementTree as ET
teams = []

matches_played = 0
start_position = 0
preloaded_ball = 0
high_goals_made_auto = 0
low_goals_made_auto = 0
shots_missed_auto = 0
hot_goal_bonus_auto = 0
moved_bonus_auto = 0
high_goals_made_tel = 0 
low_goals_made_tel = 0
shots_missed_tel = 0
balls_received_tel = 0
balls_passed_tel = 0
truss_shots_tel = 0
catches_tel = 0

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

def SaveData(team_number):
    tree = ET.parse('data.xml')
    root = tree.getroot()
    
    for team in root.findall('team'):
        if team.find('number').text == team_number:
            
            
            
            global preloaded_ball
            preloaded_ball = str(preloaded_ball) + ',' + str(team.find('preloaded_ball').text)
            
            global start_position
            start_position = str(start_position) + ',' + str(team.find('start_position').text)
            
            global matches_played
            matches_played += int(team.find('matches_played').text)
            
            global balls_passed_tel 
            balls_passed_tel += int(team.find('balls_passed_tel').text)       
            
            global catches_tel
            catches_tel += int(team.find('catches_tel').text)
            
            global truss_shots_tel
            truss_shots_tel += int(team.find('truss_shots_tel').text)
            
            global balls_passed_tel
            balls_passed_tel += int(team.find('balls_passed_tel').text)
            
            global balls_received_tel
            balls_received_tel += int(team.find('balls_received_tel').text)
            
            global shots_missed_tel
            shots_missed_tel += int(team.find('shots_missed_tel').text)
            
            global low_goals_made_tel
            low_goals_made_tel += int(team.find('low_goals_made_tel').text)
            
            global high_goals_made_tel
            high_goals_made_tel += int(team.find('high_goals_made_tel').text) 
            
            global shots_missed_auto
            shots_missed_auto += int(team.find('shots_missed_auto').text)
            
            global low_goals_made_tel
            low_goals_made_tel += int(team.find('low_goals_made_tel').text)
            
            global high_goals_made_auto
            high_goals_made_auto += int(team.find('high_goals_made_auto').text)
            
            
