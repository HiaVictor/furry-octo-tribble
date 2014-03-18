import wx
import data_interactions

teams = []

class FrcScouting(wx.Frame):
    
    def __init__(self, parent, title):
        
        self.matches_played = 0
        self.start_position = 0
        self.preloaded_ball = 0
        self.high_goals_made_auto = 0
        self.low_goals_made_auto = 0
        self.shots_missed_auto = 0
        self.hot_goal_bonus_auto = 0
        self.moved_bonus_auto = 0
        self.high_goals_made_tel = 0 
        self.low_goals_made_tel = 0
        self.shots_missed_tel = 0
        self.balls_received_tel = 0
        self.balls_passed_tel = 0
        self.truss_shots_tel = 0
        self.catches_tel = 0
        self.devensive_maneuvers_tel = 0
        self.balls_loss_tel = 0
    
        
        super(FrcScouting, self).__init__(parent, title=title, size=(1024, 400))  
        self.pnl = wx.Panel(self)
        self.title = wx.StaticText(self.pnl, label='2168 Scouting System', pos=(445,10))
        
        #-----General Objects-----#
        self.gl = wx.StaticBox(self.pnl, label='Teams', size=wx.Size(200,300), pos=(10,30))
        self.gl.Hide()
        self.team_list = wx.ListBox(self.gl, pos=(55,20), size=wx.Size(100,270))
        
        data_interactions.get_teams()
        self.show_teams(data_interactions.teams)
        self.scout_box = wx.StaticBox(self.pnl, label='Scouting Type', size = wx.Size(175,100), pos=(420,30))
        
        self.scout_match = wx.Button(self.scout_box, label='Match Scout', pos=(10,30))
        self.pit_scout = wx.Button(self.scout_box, label='Pit Scout', pos=(10, 60))
        self.view_data = wx.Button(self.scout_box, label='View Data', pos= (100, 30), size=wx.Size(60,56))
        
        
        self.scout_match.Bind(wx.EVT_BUTTON, self.MatchScout)
        self.pit_scout.Bind(wx.EVT_BUTTON, self.PitScout)
        self.view_data.Bind(wx.EVT_BUTTON, self.ViewData)
        self.team_list.Bind(wx.EVT_LISTBOX, self.SelectedTeam)
           
        #-----General Objects-----#
        
        #=========================#
        
        #-----Match Scout Objects-----#
        self.match_scout_obj = wx.StaticBox(self.pnl, label='Match Scout', size=wx.Size(700,300),pos=(250,30))
        self.matches_played = wx.StaticText(self.match_scout_obj, label='Matches Played: ????', pos=(50,50))
        self.save_data = wx.Button(self.match_scout_obj, label='Save Data', pos=(600,260))
        self.start_position_label = wx.StaticText(self.match_scout_obj, label='Start Position:', pos=(50,83))
        self.start_position_cb = wx.ComboBox(self.match_scout_obj, style=wx.CB_DROPDOWN,choices=('Center','Left','Right'),pos=(130,80))
        self.start_preloaded_ball_label = wx.StaticText(self.match_scout_obj, label='Preloaded Ball:', pos=(50,120))
        self.start_preloaded_ball_yes = wx.CheckBox(self.match_scout_obj, label='Yes', pos=(140,120))
        self.start_preloaded_ball_no = wx.CheckBox(self.match_scout_obj, label='No', pos=(180,120))
        self.high_goals_made_auto_label = wx.StaticText(self.match_scout_obj, label='Auto High Goals: 0', pos=(50,150))
        self.high_goals_made_auto_add = wx.Button(self.match_scout_obj, label='+', pos=(100,165), size=(50,25))
        self.high_goals_made_auto_sub = wx.Button(self.match_scout_obj, label='-', pos=(50,165), size=(50,25))
        self.low_goals_made_auto_label = wx.StaticText(self.match_scout_obj, label='Auto Low Goals: 0', pos=(50,200))
        self.low_goals_made_auto_add = wx.Button(self.match_scout_obj, label='+', pos=(100,215), size=(50,25))
        self.low_goals_made_auto_sub = wx.Button(self.match_scout_obj, label='-', pos=(50,215), size=(50,25))
        self.shots_missed_auto_label = wx.StaticText(self.match_scout_obj, label='Shots Missed Auto: 0', pos=(50,245))
        self.shots_missed_auto_add = wx.Button(self.match_scout_obj, label='+', pos=(100,260), size=(50,25))
        self.shots_missed_auto_sub = wx.Button(self.match_scout_obj, label='-', pos=(50,260), size=(50,25))
        self.hot_goal_bonus_label = wx.StaticText(self.match_scout_obj, label='Hot Goal: ', pos=(230,50))
        self.hot_goal_bonus_yes = wx.CheckBox(self.match_scout_obj, label='Yes', pos=(290,50))
        self.hot_goal_bonus_no = wx.CheckBox(self.match_scout_obj, label='No', pos=(330,50))
        self.moved_bonus_auto_label = wx.StaticText(self.match_scout_obj, label='Moved Bonus: ', pos=(230,83))
        self.moved_bonus_auto_yes = wx.CheckBox(self.match_scout_obj, label='Yes', pos=(310,83))
        self.moved_bonus_auto_no = wx.CheckBox(self.match_scout_obj, label='No', pos=(350,83))
        #self.high_goals_made_label = wx.StaticText(self.match_scout_obj, label='High Goals Made Teleoperation: ')
        self.match_scout_obj.Hide()
        
        self.start_preloaded_ball_yes.Bind(wx.EVT_CHECKBOX, self.PreloadedBallYesCheckBox)
        self.start_preloaded_ball_no.Bind(wx.EVT_CHECKBOX, self.PreloadedBallNoCheckBox)
        self.high_goals_made_auto_add.Bind(wx.EVT_BUTTON, self.HighGoalAutoAdd)
        self.high_goals_made_auto_sub.Bind(wx.EVT_BUTTON, self.HighGoalAutoSub)   
        self.low_goals_made_auto_add.Bind(wx.EVT_BUTTON, self.LowGoalAutoAdd)
        self.low_goals_made_auto_sub.Bind(wx.EVT_BUTTON, self.LowGoalAutoSub)
        self.shots_missed_auto_add.Bind(wx.EVT_BUTTON, self.ShotsMissedAutoAdd)
        self.shots_missed_auto_sub.Bind(wx.EVT_BUTTON, self.ShotsMissedAutoSub)
        self.hot_goal_bonus_yes.Bind(wx.EVT_CHECKBOX, self.HotGoalYesCheckBox)
        self.hot_goal_bonus_no.Bind(wx.EVT_CHECKBOX, self.HotGoalNoCheckBox)
        self.moved_bonus_auto_yes.Bind(wx.EVT_CHECKBOX, self.MovedBonusYesCheckBox)
        self.moved_bonus_auto_no.Bind(wx.EVT_CHECKBOX, self.MovedBonusNoCheckBox)
        
        self.Show()  
     
    def MovedBonusNoCheckBox(self, event):
        self.moved_bonus_auto_yes.SetValue(False)
        self.moved_bonus_auto_no.SetValue(True)
     
    def MovedBonusYesCheckBox(self, event):
        self.moved_bonus_auto_yes.SetValue(True)
        self.moved_bonus_auto_no.SetValue(False)
     
    def HotGoalNoCheckBox(self, event):
        self.hot_goal_bonus_yes.SetValue(False)
        self.hot_goal_bonus_no.SetValue(True)
           
    def HotGoalYesCheckBox(self, event):
        self.hot_goal_bonus_yes.SetValue(True)
        self.hot_goal_bonus_no.SetValue(False)
     
    def ShotsMissedAutoAdd(self, event):
        self.shots_missed_auto += int(1)
        self.shots_missed_auto_label.Label='Shots Missed Auto: ' + str(self.shots_missed_auto)
    
    def ShotsMissedAutoSub(self, event):
        self.shots_missed_auto -= int(1)
        self.shots_missed_auto_label.Label='Shots Missed Auto: ' + str(self.shots_missed_auto)
     
    def LowGoalAutoAdd(self, event):
        self.low_goals_made_auto += int(1)
        self.low_goals_made_auto_label.Label='Auto Low Goals: ' + str(self.low_goals_made_auto)
        
    def LowGoalAutoSub(self, event):
        self.low_goals_made_auto -= int(1)
        self.low_goals_made_auto_label.Label='Auto Low Goals: ' + str(self.low_goals_made_auto)
        
    def HighGoalAutoSub(self, event):
        self.high_goals_made_auto -= int(1)
        self.high_goals_made_auto_label.Label='Auto High Goals: ' + str(self.high_goals_made_auto)
        
    def HighGoalAutoAdd(self, event):
        self.high_goals_made_auto += int(1)
        self.high_goals_made_auto_label.Label='Auto High Goals: ' + str(self.high_goals_made_auto)
        
    def PreloadedBallNoCheckBox(self, event):
        self.start_preloaded_ball_no.SetValue(True)
        self.start_preloaded_ball_yes.SetValue(False)
        
    def PreloadedBallYesCheckBox(self, event):
        self.start_preloaded_ball_no.SetValue(False)
        self.start_preloaded_ball_yes.SetValue(True) 
        
    def SelectedTeam(self, event):    
        self.match_scout_obj.Enable()
        match_played = int(data_interactions.get_matches_played(self.team_list.GetStringSelection()))
        match_played += 1
        self.matches_played.Label = 'Matches Played: ' + str(match_played)
        
    
    def ViewData(self, event):  
        self.gl.Show()
        self.scout_box.Hide() 
    
    def PitScout(self, event): 
        self.gl.Show()
        self.scout_box.Hide()
    
    def MatchScout(self, event):
        self.gl.Show()
        self.scout_box.Hide()
        self.match_scout_obj.Show()
        self.match_scout_obj.Disable()
          
    def show_teams(self, team):
        for l in team:
            self.team_list.Insert(l, pos = self.team_list.GetCount())
        pass         
                     
if __name__ == '__main__': 
    app = wx.App()
    fs = FrcScouting(None, title='2168 Scouting')
    app.MainLoop()
    
