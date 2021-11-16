import mysql.connector
import os
from fer import FER
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
from kivy.core.audio import SoundLoader
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.list import MDList

mydb = mysql.connector.connect(host="localhost", user="root", passwd="abcd7718", database="rhythm")
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
from kivy.graphics.texture import Texture
import threading
from functools import partial
from kivymd.app import MDApp
from kivymd.uix.list import IconLeftWidget, IconRightWidget, ImageLeftWidget, TwoLineAvatarIconListItem, \
    TwoLineIconListItem, TwoLineAvatarListItem, ImageRightWidget, TwoLineRightIconListItem
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDRoundFlatButton
from kivy.properties import NumericProperty
from kivy.uix.image import AsyncImage, Image, CoreImage
from kivy.properties import DictProperty
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivy.lang import Builder
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.textfield import MDTextField
from kivy.app import App
from kivy.uix.label import Label
from kivymd.utils.fitimage import FitImage
import cv2
import numpy as np

from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivymd.uix.dialog import MDDialog
from kivymd.uix.behaviors import TouchBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
import time


Window.size = (350, 660)

screen_helper = """


ScreenManager:
    id:sm
    Screen:

        name:'Home'
        FloatLayout:
            canvas:
                Rectangle:
                    source: 'main.jpg'
                    size: self.size
                    pos: self.pos


            MDFillRoundFlatButton:
                text:'Lets get Started'
                pos_hint:{'center_x': 0.5, 'center_y': 0.15}
                font_size:16
                on_press:
                    app.go_to_menu()

            MDFloatingActionButton
                icon:"guitar-acoustic"
                pos_hint:{'center_x': 0.20, 'center_y': 0.8}
                user_font_size:"39sp"
                size_hint: None, None
                size: "58dp", "58dp"
                elevation_normal:10

            MDLabel:

                text:" Rhythm"
                halign:"center"
                theme_text_color:"Custom"
                font_style:"H3"
                pos_hint:{'center_x': 0.54, 'center_y': 0.8}
                text_color:1, 1, 1, 1

    Screen:
        name:'Home Page'
        BoxLayout:
            orientation:'vertical'
        

            MDToolbar:
                id:homepage_title
                title: 'Rhythm'
                elevation:10

            MDBottomNavigation:


                MDBottomNavigationItem:
                    name: 'screen 1'
                    text: 'Home'
                    icon: 'home'
                    id:homepage

                    canvas.before:
                        Color:
                            rgba: 9/255.0, 0, 0, 1
                        Rectangle:
                            size: self.size
                            pos: self.pos

                    BoxLayout:

                        canvas.before:
                            Color:
                                rgba: 9/255.0, 0, 0, 1
                            Rectangle:
                                size: self.size
                                pos: self.pos
                        spacing:20
                        padding:10,10,10,10
                        orientation:'vertical'



                        MDFlatButton:
                            pos_hint:{'center_x': 0.5, 'center_y': 0.5}
                            size_hint:1,1
                            on_press:
                                app.mood()
                            FitImage:
                                source:'detect.jpg'
                                size_hint:1,1

                        GridLayout:
                            size_hint_y: None
                            height: self.minimum_height  
                            row_default_height: 130
                            cols:2
                            padding: 10
                            spacing : 20
                            MDFlatButton:
                                text:'hi'
                                size_hint:1,1
                                on_press:
                                    app.go_to_playlist()
                                FitImage:
                                    source:'cassette.jpg'
                                    size_hint:1,1


                            MDFlatButton:
                                text:'hi'
                                size_hint:1,1
                                on_press:
                                    app.go_to_language()
                                FitImage:
                                    source:'language.jpg'
                                    size_hint:1,1

                            MDFlatButton:
                                text:'hi'
                                size_hint:1,1
                                on_press:
                                    app.newuser()
                                FitImage:
                                    source:'user.jpg'
                                    size_hint:1,1

                            MDFlatButton:
                                text:'hi'
                                size_hint:1,1
                                on_press:
                                    sm.current='stats'
                                    app.statistics()
                                    
                                FitImage:
                                    source:'data.jpg'
                                    size_hint:1,1



                MDBottomNavigationItem:
                    text: 'Favourites'
                    icon: 'heart'
                    on_tab_release: app.show_fav_songs()

                    canvas.before:
                        Color:
                            rgba: 9/255.0, 0, 0, 1
                        Rectangle:
                            size: self.size
                            pos: self.pos

                    MDBoxLayout:
                        orientation: "vertical"
                        ScrollView:
                            canvas.before:
                                Color:
                                    rgba: 9/255.0, 0, 0, 1
                                Rectangle:
                                    size: self.size
                                    pos: self.pos

                            MDList:
                                padding: 5,0,25,0
                                id: fav_id 
                                size_hint_y: None
                                height: self.minimum_height

                MDBottomNavigationItem:
                    name:"hi"
                    text: 'Most Played'
                    icon: 'playlist-music-outline'
                    on_tab_release: app.show_played_songs()
                    
                    MDTabs:
                        Tab:
                            text:'Neutral'
                            MDBoxLayout:
                                orientation: "vertical"
                                ScrollView:
                                    canvas.before:
                                        Color:
                                            rgba: 9/255.0, 0, 0, 1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
        
                                    MDList:
                                        padding: 5,0,25,0
                                        id: neutral
                                        size_hint_y: None
                                        height: self.minimum_height
                            
                            
                        
                        Tab:
                            text:'Happy'
                            MDBoxLayout:
                                orientation: "vertical"
                                ScrollView:
                                    canvas.before:
                                        Color:
                                            rgba: 9/255.0, 0, 0, 1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
        
                                    MDList:
                                        padding: 5,0,25,0
                                        id: happy 
                                        size_hint_y: None
                                        height: self.minimum_height
                            
                        Tab:
                            text:'Sad'
                            MDBoxLayout:
                                orientation: "vertical"
                                ScrollView:
                                    canvas.before:
                                        Color:
                                            rgba: 9/255.0, 0, 0, 1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
        
                                    MDList:
                                        padding: 5,0,25,0
                                        id: sad
                                        size_hint_y: None
                                        height: self.minimum_height
                        
                        Tab:
                            text:'Angry'
                            MDBoxLayout:
                                orientation: "vertical"
                                ScrollView:
                                    canvas.before:
                                        Color:
                                            rgba: 9/255.0, 0, 0, 1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
        
                                    MDList:
                                        padding: 5,0,25,0
                                        id:angry
                                        size_hint_y: None
                                        height: self.minimum_height
                        
                        Tab:
                            text:'Fear'
                            MDBoxLayout:
                                orientation: "vertical"
                                ScrollView:
                                    canvas.before:
                                        Color:
                                            rgba: 9/255.0, 0, 0, 1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
        
                                    MDList:
                                        padding: 5,0,25,0
                                        id: fear
                                        size_hint_y: None
                                        height: self.minimum_height
                        
                        Tab:
                            text:'Surprise'
                            MDBoxLayout:
                                orientation: "vertical"
                                ScrollView:
                                    canvas.before:
                                        Color:
                                            rgba: 9/255.0, 0, 0, 1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
        
                                    MDList:
                                        padding: 5,0,25,0
                                        id: surprise
                                        size_hint_y: None
                                        height: self.minimum_height
                        
                        Tab:
                            text:'Disgust'
                            MDBoxLayout:
                                orientation: "vertical"
                                ScrollView:
                                    canvas.before:
                                        Color:
                                            rgba: 9/255.0, 0, 0, 1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
        
                                    MDList:
                                        padding: 5,0,25,0
                                        id: disgust
                                        size_hint_y: None
                                        height: self.minimum_height
                        


    Screen:
        name:'language'      

        FloatLayout:
            id:lang
            canvas:
                Rectangle:
                    source: 'home1.jpg'
                    size: self.size
                    pos: self.pos

            MDLabel:
                text:"Choose Language?"
                halign:"center"
                theme_text_color:"Primary"
                font_style:"H5"
                pos_hint:{'center_x': 0.5, 'center_y': 0.5}

            MDToolbar:                

                title: "Language"
                # left_action_items: [["arrow-left", lambda x: app.go_back_to_menu()]]
                right_action_items: [["arrow-right", lambda x: app.next1()]]
                elevation: 10
                pos_hint:{'center_x': 0.5, 'center_y': 0.95}

    Screen:
        name:'Menu'

        FloatLayout:

            canvas:
                Rectangle:
                    source: 'home1.jpg'
                    size: self.size
                    pos: self.pos

            MDTextField:
                id: input
                hint_text: "Enter Username"
                max_text_length: 10
                helper_text: "Please enter a Short Username"
                helper_text_mode: "on_error"
                icon_right: "guitar-acoustic"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.75}
                size_hint_x:None
                width:300


            MDLabel:
                text:"What's your name?"
                halign:"center"
                theme_text_color:"Primary"
                font_style:"H5"
                pos_hint:{'center_x': 0.5, 'center_y': 0.9}

            MDLabel:
                text:"Choose Language?"
                halign:"center"
                theme_text_color:"Primary"
                font_style:"H5"
                pos_hint:{'center_x': 0.5, 'center_y': 0.5}



            MDRaisedButton:
                text:"Next" 
                pos_hint: {'center_x': 0.85, 'center_y': 0.05}
                size_hint :0.2 , 0.06
                font_size: 20
                text_color: 1,1,1,1
                md_bg_color: 0.137, 0.654, 0.941, 1
                font_name:'Candara'
                on_release:
                    app.next(input.text)

            FloatLayout:
                id: menu_id



    Screen:
        name:'playlist'

        MDBoxLayout:
            orientation: "vertical"
            MDToolbar:                

                title: "Select Playlist"
                # left_action_items: [["arrow-left", lambda x: app.go_back_to_menu()]]
                right_action_items: [["arrow-right", lambda x: app.go_to_camera()]]
                elevation: 10


            ScrollView:
                canvas.before:
                    Color:
                        rgba: 9/255.0, 0, 0, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos

                GridLayout:
                    id:playlist1
                    size_hint_y: None
                    height: self.minimum_height  
                    row_default_height: 140
                    cols:2
                    padding: 25
                    spacing : 20


    Screen:
        name:'Camera'
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 9/255.0, 0, 0, 1
            Rectangle:
                size: self.size
                pos: self.pos
        MDLabel:
            text:"Photo will be clicked shortly"
            halign:"center"
            theme_text_color:"Primary"
            font_style:"H5"
            pos_hint:{'center_x': 0.5, 'center_y': 0.85}

        MDLabel:
            text:"        (Note: If 0 or multiple faces are found, the counter will re-run)"
            halign:"center"
            theme_text_color:"Primary"
            font_size:12
            pos_hint:{'center_x': 0.46, 'center_y': 0.15}

        Image:
            # this is where the video will show
            # the id allows easy access
            id: vid
            size_hint: 1, 0.6
            allow_stretch: True  # allow the video image to be scaled
            keep_ratio: True  # keep the aspect ratio so people don't look squashed
            pos_hint: {'center_x':0.5, 'top':0.8}   


    Screen:
        name: 'show_emotions'
        canvas.before:
            Color:
                rgba: 232/255.0, 240/255.0, 253/255.0, 1
            Rectangle:
                size: self.size
                pos: self.pos

        MDBoxLayout:
            orientation: "vertical"
            MDToolbar:                
                title: "Emotions Detected"
                right_action_items: [["arrow-right", lambda x: app.go_to_songs()]]
                elevation: 10


            MDBoxLayout:
                orientation: "vertical"
                spacing: 50
                padding: 50

                MDIcon:
                    id: image_id
                    icon: "Eminem.jpg"
                    allow_stretch: True
                    keep_ratio: False
                    # size_hint_x: 0.75
                    # size_hint_y: 0.4

                MDBoxLayout:
                    id: mood_id
                    orientation: "vertical"
                    spacing: 20
                    padding: 00


    Screen:
        name:'songs'

        canvas.before:
            Color:
                rgba: 9/255.0, 0, 0, 1
            Rectangle:
                size: self.size
                pos: self.pos

        MDBoxLayout:
            orientation: "vertical"
            MDToolbar:
                title: "Songs for you!"
                elevation: 10
                left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]



            ScrollView:
                canvas.before:
                    Color:
                        rgba: 9/255.0, 0, 0, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
                MDList:
                    padding: 5,0,25,0

                    id: song_id 
                    size_hint_y: None
                    height: self.minimum_height  



        MDNavigationDrawer:
            id: nav_drawer  
            MDBoxLayout:
                orientation: "vertical"
                spacing: "10dp"
                padding: "18dp"

                AnchorLayout:
                    anchor_x: "left"
                    size_hint_y: None
                    height: avatar.height


                    MDFloatingActionButton
                        id: avatar
                        icon:"account"
                        md_bg_color: app.theme_cls.primary_color
                        user_font_size: "65sp"
                        size_hint: None, None
                        size: "100dp", "100dp"
                        elevation_normal:10

                MDLabel:

                    text: "  Hi, " + input.text + " !"
                    theme_text_color:"Primary"
                    font_size: 20
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: " "
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: " "
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]


                ScrollView:
                    MDList:
                        OneLineAvatarIconListItem:
                            text: "Home"
                            on_press:
                                nav_drawer.set_state("close")
                                app.stop_song()
                                app.go_to_menu()
                            IconLeftWidget:
                                icon: "home"



                        OneLineAvatarIconListItem:
                            text: "Exit"
                            on_press: 
                                nav_drawer.set_state("close")
                                app.exit_app()
                            IconLeftWidget:
                                icon: "logout"


    Screen:
        name:'stats'
        canvas.before:
            Color:
                rgba: 1,1,1,1
            Rectangle:
                size: self.size
                pos: self.pos
        FloatLayout:
            MDToolbar:                

                title: "Mood Statistics"
                left_action_items: [["arrow-left", lambda x: app.go_to_camera()]]
                #right_action_items: [["arrow-right", lambda x: app.next1()]]
                elevation: 10
                pos_hint:{'center_x': 0.5, 'center_y': 0.95}
            
            FloatLayout:
                id:mood_stats1
            FloatLayout:
                id:mood_stats2


<Tab>

"""

# Font size in descending order to print moods from highest to lowest %
fonts = ["H4", "H5", "H5", "H6", "H6", "Subtitle1", "Subtitle2"]

mycursor = mydb.cursor(buffered=True)

mycursor.execute("select * from lang_user")
lang = mycursor.fetchall()
lang = [item for t in lang for item in t]
print(lang)

mycursor.execute("select * from play_user")
play_list = mycursor.fetchall()
play_list = [item for t in play_list for item in t]
print(play_list)

mycursor.execute("select * from fav")
fav_songs = mycursor.fetchall()
fav_songs = [item for t in fav_songs for item in t]
print(fav_songs)

mycursor.execute("select * from username")
user = mycursor.fetchall()


# aa= [item for t in user for item in t]
# username = aa[0]


# Create the screen manager
class Tab(FloatLayout, MDTabsBase):
    pass

class DemoApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.screen = Builder.load_string(screen_helper)
        return self.screen

    # ----------------------------------------------------------------------------------------------------------------
    # Photo and Emotion Percentage

    def emotion_page(self):
        self.root.ids.mood_id.clear_widgets()
        self.root.ids.image_id.icon = "testcases/IMG_{}.png".format(self.timestr)

        detector = FER()
        self.image = cv2.imread("testcases/IMG_{}.png".format(self.timestr))
        result = detector.detect_emotions(self.image)

        dict = (result[0]['emotions'])
        sorted_tuples = sorted(dict.items(), key=lambda item: item[1])
        print(sorted_tuples)

        pp = 6
        for i in range(7):
            emot = MDLabel(text=sorted_tuples[pp - i][0] + " - " + str(sorted_tuples[pp - i][1] * 100)[0:4] + " %",
                           theme_text_color="Custom", text_color=[0, 0, 0, 1], font_style=fonts[i], halign="center")
            print("Emotion - ", emot.text)
            self.root.ids.mood_id.add_widget(emot)

    # --------------------------------------------------------------------------------------------------------------------
    # Display Song List by Mood

    def song_page(self):
        self.root.ids.song_id.clear_widgets()
        # image = cv2.imread("testcases/IMG_{}.png".format(self.timestr))

        detector = FER()

        self.topmood = detector.top_emotion(self.image)
        print("Topmood: ", self.topmood[0])
        mycursor.execute("update mood_count set count=count+1 where mood='" + self.topmood[0] + "';")
        mydb.commit()
        for i in range(len(play_list)):
            print(play_list[i])
            mycursor.execute(
                "select song_list.song,song_list.song_img from playlist inner join song_list where "
                "playlist.play_id=song_list.play_id AND play ='" +
                play_list[i] + "' AND emotion = '" + self.topmood[0] + "';")
            res = mycursor.fetchall()

            for j in range(len(res)):
                print(res[j][0])
                img1 = ImageLeftWidget(source="songs/" + self.topmood[0] + "_songs/" + res[j][1])
                img2 = IconRightWidget(icon="heart", theme_text_color="Custom",
                                       text_color=[1, 1, 1, 1], on_release=self.add_to_liked_songs)
                if res[j][0] in fav_songs:
                    img2.theme_text_color = "Custom"
                    img2.text_color = [1, 0, 0, 1]

                img3 = IconRightWidget(icon="play", padding=20, on_release=self.fav)
                songs = TwoLineAvatarIconListItem(text="" + res[j][0], font_style="Subtitle1",
                                                  secondary_text="" + play_list[i], secondary_font_style="Caption",
                                                  on_release=self.play)
                songs.add_widget(img1)
                songs.add_widget(img2)
                songs.add_widget(img3)
                self.root.ids.song_id.add_widget(songs)

    # --------------------------------------------------------------------------------------------------------------------
    # Display Singers by selected language

    def playlist_page(self):
        self.root.ids.playlist1.clear_widgets()
        for i in range(len(lang)):
            print(lang[i])
            mycursor.execute(
                "select playlist.play,playlist.play_img from playlist inner join language where "
                "playlist.lang_id=language.lang_id AND lang ='" + lang[i] + "';")
            res = mycursor.fetchall()

            for j in range(len(res)):
                self.btn = MDFlatButton(text=res[j][0], size_hint=(0.3, 0.3), on_press=self.update_playlist)
                self.img = AsyncImage(source="playlists/" + lang[i] + "_playlists/" + res[j][1], color=[1, 1, 1, 1])
                self.btn.add_widget(self.img)
                if self.btn.text in play_list:
                    self.btn.md_bg_color = [1, 1, 1, 0.5]
                self.root.ids.playlist1.add_widget(self.btn)

    # --------------------------------------------------------------------------------------------------------------------
    # Select Language and append in lang[]
    def language(self):
        btn1 = MDRoundFlatButton(
            text="Marathi",
            pos_hint={'center_x': 0.35, 'center_y': 0.36},
            size_hint=(0.25, 0.06),
            font_size=20,
            text_color=[0.137, 0.654, 0.941, 1],
            md_bg_color=[0.137, 0.654, 0.941, 0],
            #elevation_normal=10,
            on_press=self.update2)

        if btn1.text in lang:
            btn1.md_bg_color = [1, 1, 1, 0.2]

        btn2 = MDRoundFlatButton(
            text="Hindi",
            pos_hint={'center_x': 0.65, 'center_y': 0.25},
            size_hint=(0.25, 0.06),
            font_size=20,
            text_color=[0.137, 0.654, 0.941, 1],
            md_bg_color=[0.137, 0.654, 0.941, 0],
            #elevation_normal=10,
            on_press=self.update2)

        if btn2.text in lang:
            btn2.md_bg_color = [1, 1, 1, 0.2]

        btn3 = MDRoundFlatButton(
            text="English",
            pos_hint={'center_x': 0.35, 'center_y': 0.25},
            size_hint=(0.25, 0.06),
            font_size=20,
            text_color=[0.137, 0.654, 0.941, 1],
            md_bg_color=[0.137, 0.654, 0.941, 0],
            #elevation_normal=10,
            on_press=self.update2)

        if btn3.text in lang:
            btn3.md_bg_color = [1, 1, 1, 0.2]

        btn4 = MDRoundFlatButton(
            text="Punjabi",
            pos_hint={'center_x': 0.65, 'center_y': 0.36},
            size_hint=(0.25, 0.06),
            font_size=20,
            text_color=[0.137, 0.654, 0.941, 1],
            md_bg_color=[0.137, 0.654, 0.941, 0],
            #elevation_normal=10,
            on_press=self.update2)

        if btn4.text in lang:
            btn4.md_bg_color = [1, 1, 1, 0.2]

        self.root.ids.lang.add_widget(btn1)
        self.root.ids.lang.add_widget(btn2)
        self.root.ids.lang.add_widget(btn3)
        self.root.ids.lang.add_widget(btn4)

    def update2(self, id):
        for i in lang:
            if i == id.text:
                id.md_bg_color = [1, 1, 1, 0]
                lang.remove(id.text)
                mycursor.execute("delete from lang_user where language = '" + id.text + "';")
                mydb.commit()
                print(lang)
                return

        id.md_bg_color = [1, 1, 1, 0.2]
        lang.append(id.text)
        mycursor.execute("insert into lang_user value('" + id.text + "');")
        mydb.commit()
        print(lang)

    def update1(self, id):
        for i in lang:
            if i == id:
                MDFlatButton.md_bg_color = [1, 1, 1, 0]
                lang.remove(id)
                mycursor.execute("delete from lang_user where language = '" + id + "';")
                mydb.commit()
                print(lang)
                return

        MDFlatButton.md_bg_color = [1, 1, 1, 0.2]
        lang.append(id)
        mycursor.execute("insert into lang_user value('" + id + "');")
        mydb.commit()
        print(lang)

    # --------------------------------------------------------------------------------------------------------------------
    # Select singer and append in playlist[]

    def update_playlist(self, hi):
        for i in play_list:
            if (i == hi.text):
                hi.md_bg_color = [1, 1, 1, 0]
                print(hi.md_bg_color)
                play_list.remove(hi.text)
                mycursor.execute("delete from play_user where playlist_user = '" + hi.text + "';")
                mydb.commit()
                print("removed")
                return

        hi.md_bg_color = [1, 1, 1, 0.5]
        print(hi.md_bg_color)
        play_list.append(hi.text)
        mycursor.execute("insert into play_user value('" + hi.text + "');")
        mydb.commit()
        print(hi.text + " Added")

    # --------------------------------------------------------------------------------------------------------------------
    # Checking if lang and username is given input

    def next(self, text):
        username = text
        if username is "":
            user_error = "Please enter Your Username"
            self.dialog = MDDialog(
                text=user_error, size_hint=(0.7, 1),
                buttons=[MDRaisedButton(text='OK', on_release=self.close_dialog)]
            )
            self.dialog.open()

        elif ' ' in username:
            user_error = "No spaces allowed"
            self.dialog = MDDialog(
                text=user_error, size_hint=(0.52, 1),
                buttons=[MDRaisedButton(text='OK', on_release=self.close_dialog)]
            )
            self.dialog.open()

        elif len(username) > 10:
            user_error = "Please enter a Short Username"
            self.dialog = MDDialog(
                text=user_error, size_hint=(0.74, 1),
                buttons=[MDRaisedButton(text='OK', on_release=self.close_dialog)]
            )
            self.dialog.open()

        # if it contains no alphabets at all
        elif not any(c.isalpha() for c in username):
            print("")
            user_error = "Minimun One alphabet is required"
            self.dialog = MDDialog(
                text=user_error, size_hint=(0.8, 1),
                buttons=[MDRaisedButton(text='OK', on_release=self.close_dialog)]
            )
            self.dialog.open()
        elif not lang:
            user_error = "Please select Language"
            self.dialog = MDDialog(
                text=user_error, size_hint=(0.62, 1),
                buttons=[MDRaisedButton(text='OK', on_release=self.close_dialog)]
            )
            self.dialog.open()

        else:
            mycursor.execute("insert into username value('" + username + "');")
            mydb.commit()
            self.root.transition.direction = 'left'
            self.root.current = 'playlist'
            self.a = len(lang)
            self.playlist_page()

        print(username)

    def next1(self):
        if not lang:
            user_error = "Please select Language"
            self.dialog = MDDialog(
                text=user_error, size_hint=(0.62, 1),
                buttons=[MDRaisedButton(text='OK', on_release=self.close_dialog)]
            )
            self.dialog.open()

        else:
            self.root.transition.direction = 'left'
            self.root.current = 'playlist'
            self.a = len(lang)
            self.playlist_page()

    # --------------------------------------------------------------------------------------------------------------------
    # To close dialog Box
    def newuser(self):
        user_error = "It will clear your all your previous data ! Are you sure you want to change user?"
        self.dialog = MDDialog(
            text=user_error, size_hint=(0.62, 1),
            buttons=[MDRaisedButton(text='No', on_release=self.close_dialog),
                     MDRaisedButton(text='Yes, I,m sure', on_release=self.clear_data)]

        )
        self.dialog.open()

    def clear_data(self, hi):

        self.dialog.dismiss()
        mycursor.execute("delete from play_user")
        mydb.commit()
        play_list.clear()

        mycursor.execute("delete from lang_user")
        mydb.commit()
        lang.clear()

        mycursor.execute("delete from fav")
        mydb.commit()
        fav_songs.clear()

        mycursor.execute("delete from played_songs")
        mydb.commit()

        mycursor.execute("Update mood_count set count = 0;")
        mydb.commit()

        mycursor.execute("delete from username")
        mydb.commit()
        user.clear()
        mycursor.execute("select * from username")
        uu=mycursor.fetchall()
        print("ABCD" + str(uu))

        self.go_to_menu()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    # --------------------------------------------------------------------------------------------------------------------
    # Face Detection

    def doit(self):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # this code is run in a separate thread
        self.do_vid = True  # flag to stop loop

        # make a window for use by cv2
        # flags allow resizing without regard to aspect ratio
        cv2.namedWindow('Hidden', cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)

        # resize the window to (0,0) to make it invisible
        cv2.resizeWindow('Hidden', 0, 0)
        cam = cv2.VideoCapture(0)

        # start processing loop
        while (self.do_vid):

            ret, img = cam.read()
            Clock.schedule_once(partial(self.display_frame, img))

            # cv2.imshow('Hidden', img)
            k = cv2.waitKey(125)
            prev = time.time()
            TIMER = int(3)
            while TIMER >= 0:
                ret, img = cam.read()
                grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                face = face_cascade.detectMultiScale(grayimg, 1.1, 4)
                for (x, y, w, h) in face:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # Display countdown on each frame, specify the font and draw the countdown using puttext
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, str(TIMER),
                            (25, 450), font,
                            2, (255, 255, 255),
                            4, cv2.LINE_AA)
                cv2.waitKey(125)

                # current time
                cur = time.time()

                # Update and keep track of Countdown, if time elapsed is one second then decrease the counter
                if cur - prev >= 1:
                    prev = cur
                    TIMER = TIMER - 1
                Clock.schedule_once(partial(self.display_frame, img))

            else:
                self.timestr = time.strftime("%Y%m%d_%H%M%S")
                cv2.imwrite("testcases/IMG_{}.png".format(self.timestr), img)
                break

        if len(face) == 1:
            cam.release()
            cv2.destroyAllWindows()
            self.root.current = 'show_emotions'
            self.emotion_page()

        else:
            self.doit()

    # --------------------------------------------------------------------------------------------------------------------
    # Stop Video Loop on screen

    def stop_vid(self):
        self.do_vid = False

    # --------------------------------------------------------------------------------------------------------------------
    # Display opencv screen in kivy screen

    def display_frame(self, frame, dt):

        # create a Texture the correct size and format for the frame
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')

        # copy the frame data into the texture
        texture.blit_buffer(frame.tobytes(order=None), colorfmt='bgr', bufferfmt='ubyte')

        # flip the texture (otherwise the video is upside down
        texture.flip_vertical()

        # actually put the texture in the kivy Image widget
        self.root.ids.vid.texture = texture

    # --------------------------------------------------------------------------------------------------------------------
    # Lets Go Button

    def go_to_menu(self):
        mycursor.execute("select * from username")
        user = mycursor.fetchall()
        print("helooooo")
        if not user:

            self.root.transition.direction = 'left'
            self.menu_screen()
            self.root.current = 'Menu'
            print("helooooo1")

            self.root.ids.input.bind(
                on_text_validate=self.set_error_message,
                on_focus=self.set_error_message,
            )

        else:
            self.root.current = 'Home Page'
            self.homepage()

    def homepage(self):
        mycursor.execute("select * from username")
        ab = mycursor.fetchall()
        if not ab :
            print("--If--")
            aa1 = [item for t in ab for item in t]
            self.root.ids.homepage_title.title="Welcome, " + aa1[0] + " !"

        elif not user:
            print("--elIf--")
            aa1 = [item for t in ab for item in t]
            self.root.ids.homepage_title.title = "Welcome, " + aa1[0] + " !"

        else:
            print("--else--")
            aa = [item for t in ab for item in t]
            self.root.ids.homepage_title.title = "Welcome back, " + aa[0] + " !"

    def menu_screen(self):

        self.root.ids.menu_id.clear_widgets()
        print("helooooo2")
        btn11 = MDRoundFlatButton(
            text="Marathi",
            pos_hint={'center_x': 0.35, 'center_y': 0.36},
            size_hint=(0.25, 0.06),
            font_size=20,
            text_color=[0.137, 0.654, 0.941, 1],
            md_bg_color=[0.137, 0.654, 0.941, 0],
            # elevation_normal=10,
            on_release=self.update2
        )
        print("helooooo22")
        if btn11.text in lang:
            btn11.md_bg_color = [1, 1, 1, 0.2]
        print("helooooo222")
        btn2 = MDRoundFlatButton(
            text="Hindi",
            pos_hint={'center_x': 0.65, 'center_y': 0.25},
            size_hint=(0.25, 0.06),
            font_size=20,
            text_color=[0.137, 0.654, 0.941, 1],
            md_bg_color=[0.137, 0.654, 0.941, 0],
            # elevation_normal=10,
            on_press=self.update2)

        if btn2.text in lang:
            btn2.md_bg_color = [1, 1, 1, 0.2]

        btn3 = MDRoundFlatButton(
            text="English",
            pos_hint={'center_x': 0.35, 'center_y': 0.25},
            size_hint=(0.25, 0.06),
            font_size=20,
            text_color=[0.137, 0.654, 0.941, 1],
            md_bg_color=[0.137, 0.654, 0.941, 0],
            # elevation_normal=10,
            on_press=self.update2)

        if btn3.text in lang:
            btn3.md_bg_color = [1, 1, 1, 0.2]

        btn4 = MDRoundFlatButton(
            text="Punjabi",
            pos_hint={'center_x': 0.65, 'center_y': 0.36},
            size_hint=(0.25, 0.06),
            font_size=20,
            text_color=[0.137, 0.654, 0.941, 1],
            md_bg_color=[0, 0, 0, 0],
            # elevation_normal=10,
            on_press=self.update2)

        if btn4.text in lang:
            btn4.md_bg_color = [1, 1, 1, 0.2]

        print("helooooo3")
        self.root.ids.menu_id.add_widget(btn11)
        self.root.ids.menu_id.add_widget(btn2)
        self.root.ids.menu_id.add_widget(btn3)
        self.root.ids.menu_id.add_widget(btn4)

    # --------------------------------------------------------------------------------------------------------------------
    # From Playlist back to Menu

    def go_back_to_menu(self):

        play_list.clear()
        self.root.transition.direction = 'right'
        self.root.current = 'Menu'

    def go_to_playlist(self):

        # self.root.transition.direction = 'right'
        self.root.current = 'playlist'
        self.playlist_page()

    def go_to_language(self):

        # self.root.transition.direction = 'right'
        play_list.clear()
        mycursor.execute("delete from play_user")
        mydb.commit()
        self.root.current = 'language'
        self.language()

    # --------------------------------------------------------------------------------------------------------------------
    # If playlist id not selected

    def go_to_camera(self):

        if not play_list:
            user_error = "No Playlist is Selected"
            self.dialog = MDDialog(text=user_error, size_hint=(0.58, 1),
                                   buttons=[MDRaisedButton(text='OK', on_release=self.close_dialog)])
            self.dialog.open()

        else:
            self.root.transition.direction = 'left'
            print("Else !!!!")
            self.homepage()
            self.root.current = 'Home Page'


    def mood(self):
        threading.Thread(target=self.doit, daemon=True).start()
        self.root.current = 'Camera'

    # --------------------------------------------------------------------------------------------------------------------
    # To go from emotion percentage page to songs list

    def go_to_songs(self):

        self.root.transition.direction = 'left'
        self.root.current = 'songs'
        self.song_page()

    # --------------------------------------------------------------------------------------------------------------------
    # To back to song page

    def go_back_to_songs(self):
        self.root.transition.direction = 'right'
        self.root.current = 'songs'
        self.song_page()

    # --------------------------------------------------------------------------------------------------------------------
    # To play Music

    def play(self, hi):

        print(hi.parent.parent.text)
        # load the mp3 music
        # try:
        #   self.nowPlaying.stop()
        # except:
        #   pass
        # finally:
        #   print(hi.text)
        #   self.nowPlaying = SoundLoader.load(hi.text + ".mp3")
        #   self.nowPlaying.play()

    # --------------------------------------------------------------------------------------------------------------------
    # stop playing song

    def stop_song(self):
        pass

    # --------------------------------------------------------------------------------------------------------------------
    # To play and pause the song

    def fav(self, hii):
        print("Heloo welcome to play")
        if hii.icon == "play":
            hii.icon = "pause"
            mycursor.execute("insert ignore into played_songs value('" + hii.parent.parent.text + "');")
            mydb.commit()
        else:
            hii.icon = "play"

    # --------------------------------------------------------------------------------------------------------------------
    # Show error if Username length > 10

    def set_error_message(self, instance_textfield):
        self.screen.ids.text_field_error.error = True

    # --------------------------------------------------------------------------------------------------------------------
    # To add the liked songs in a list

    def add_to_liked_songs(self, hii):
        print("Heloo welcome to fav")
        # To add the liked songs in a list
        if hii.text_color == [1, 0, 0, 1]:
            fav_songs.remove(hii.parent.parent.text)
            mycursor.execute("delete from fav where fav_song = '" + hii.parent.parent.text + "';")
            mydb.commit()
            hii.theme_text_color = "Custom"
            hii.text_color = [1, 1, 1, 1]

        # To remove the liked songs in a list
        else:
            fav_songs.append(hii.parent.parent.text)
            mycursor.execute("insert into fav value('" + hii.parent.parent.text + "');")
            mydb.commit()
            hii.theme_text_color = "Custom"
            hii.text_color = [1, 0, 0, 1]

    # --------------------------------------------------------------------------------------------------------------------
    # Display the liked songs

    def show_fav_songs(self):

        print(fav_songs)
        print(len(fav_songs))
        self.root.ids.fav_id.clear_widgets()

        for i in range(len(fav_songs)):
            print(fav_songs[i])
            print(i)
            mycursor.execute(
                "select song_list.song, song_list.song_img, playlist.play, song_list.emotion from playlist inner join "
                "song_list where playlist.play_id=song_list.play_id AND song = '" + fav_songs[i] + "';")

            print("hello" + str(i) + "aa")

            res = mycursor.fetchone()

            print(res)
            img1 = ImageLeftWidget(source="songs/" + res[3] + "_songs/" + res[1])
            img2 = IconRightWidget(icon="heart", theme_text_color="Custom",
                                   text_color=[1, 1, 1, 1], on_release=self.add_to_liked_songs)
            if res[0] in fav_songs:
                img2.theme_text_color = "Custom"
                img2.text_color = [1, 0, 0, 1]
            liked_songs = TwoLineAvatarIconListItem(text="" + res[0], font_style="Subtitle1",
                                                    secondary_text=" " + res[2], secondary_font_style="Caption",
                                                    on_release=self.play)
            img3 = IconRightWidget(icon="play", padding=20, on_release=self.fav)
            liked_songs.add_widget(img1)
            liked_songs.add_widget(img2)
            liked_songs.add_widget(img3)
            self.root.ids.fav_id.add_widget(liked_songs)

    # --------------------------------------------------------------------------------------------------------------------
    # Exit the App

    def exit_app(self):
        DemoApp().stop()

    def statistics(self):
        dir = 'C:/Users/shree/PycharmProjects/rhythm/Diagram'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        timee = time.strftime("%Y%m%d_%H%M%S")
        print("abc")
        self.root.ids.mood_stats1.clear_widgets()
        self.root.ids.mood_stats2.clear_widgets()
        mycursor.execute(
            "SELECT mood, floor(count * 100 / t.s) AS `percent of total`FROM mood_count CROSS JOIN (SELECT SUM(count) AS s FROM mood_count) t;")
        mood_per = mycursor.fetchall()
        mood_per = [str(item) for t in mood_per for item in t]
        for i in range(7):
            mood_per[i: i + 2] = [' - '.join(mood_per[i: i + 2])]

        labels = [s + "%" for s in mood_per]
        print(labels)
        mycursor.execute("select count from mood_count")
        aa = mycursor.fetchall()
        sizes = [item for t in aa for item in t]
        print(sizes)
        plt.figure(0)
        colors = ['yellow', 'gray', 'deepskyblue', 'beige', 'red', 'forestgreen', 'black']
        patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
        plt.legend(patches, labels, loc=(1.05, 0.3), fontsize=12)
        plt.axis('equal')
        plt.tight_layout()

        plt.savefig("Diagram/abc_{}.jpg".format(timee))
        print("abc")
        # -------------------------

        mycursor.execute("select mood from mood_count")
        moods = mycursor.fetchall()
        moods = [str(item) for t in moods for item in t]
        plt.figure(1)
        fig = plt.figure(figsize=(10, 8.5))

        # creating the bar plot
        plt.bar(moods, sizes, color='deepskyblue',
                width=0.4)
        plt.xlabel("MOOD", fontsize=22, labelpad=25)
        plt.ylabel("FREQUENCY", fontsize=22, labelpad=25)
        plt.xticks(fontsize=18)  # fontsize of the tick labels
        plt.yticks(fontsize=18)
        plt.title("Frequency of Different Mood", fontsize=30, pad=10, fontweight="bold")
        plt.savefig("Diagram/abcd_{}.jpg".format(timee))

        img1 = Image(source="Diagram/abcd_{}.jpg".format(timee),
                     size_hint=(1, 1),
                     pos_hint={'center_x': 0.52, 'center_y': 0.3})
        img = Image(source="Diagram/abc_{}.jpg".format(timee),
                    size_hint=(1, 1),
                    pos_hint={'center_x': 0.48, 'center_y': 0.7})

        self.root.ids.mood_stats1.add_widget(img)
        self.root.ids.mood_stats2.add_widget(img1)

    def show_played_songs(self):

        self.root.ids.happy.clear_widgets()
        self.root.ids.sad.clear_widgets()
        self.root.ids.neutral.clear_widgets()
        self.root.ids.disgust.clear_widgets()
        self.root.ids.surprise.clear_widgets()
        self.root.ids.fear.clear_widgets()
        self.root.ids.angry.clear_widgets()

        mycursor.execute(
            "select song_list.song, song_list.song_img, playlist.play from playlist inner join "
            "song_list where playlist.play_id=song_list.play_id AND song in (select * from played_songs) AND emotion ='happy';")
        res=mycursor.fetchall()
        for i in range(len(res)):
            img1 = ImageLeftWidget(source="songs/happy_songs/" + res[i][1])
            img2 = IconRightWidget(icon="heart", theme_text_color="Custom",
                                   text_color=[1, 1, 1, 1], on_release=self.add_to_liked_songs)
            if res[i][0] in fav_songs:
                img2.theme_text_color = "Custom"
                img2.text_color = [1, 0, 0, 1]
            liked_songs = TwoLineAvatarIconListItem(text="" + res[i][0], font_style="Subtitle1",
                                                    secondary_text=" " + res[i][2], secondary_font_style="Caption",
                                                    on_release=self.play)
            img3 = IconRightWidget(icon="play", padding=20, on_release=self.fav)
            liked_songs.add_widget(img1)
            liked_songs.add_widget(img2)
            liked_songs.add_widget(img3)
            self.root.ids.happy.add_widget(liked_songs)

        mycursor.execute(
            "select song_list.song, song_list.song_img, playlist.play from playlist inner join "
            "song_list where playlist.play_id=song_list.play_id AND song in (select * from played_songs) AND emotion ='neutral';")
        res = mycursor.fetchall()
        for i in range(len(res)):
            img1 = ImageLeftWidget(source="songs/neutral_songs/" + res[i][1])
            img2 = IconRightWidget(icon="heart", theme_text_color="Custom",
                                   text_color=[1, 1, 1, 1], on_release=self.add_to_liked_songs)
            if res[i][0] in fav_songs:
                img2.theme_text_color = "Custom"
                img2.text_color = [1, 0, 0, 1]
            liked_songs = TwoLineAvatarIconListItem(text="" + res[i][0], font_style="Subtitle1",
                                                    secondary_text=" " + res[i][2], secondary_font_style="Caption",
                                                    on_release=self.play)
            img3 = IconRightWidget(icon="play", padding=20, on_release=self.fav)
            liked_songs.add_widget(img1)
            liked_songs.add_widget(img2)
            liked_songs.add_widget(img3)
            self.root.ids.neutral.add_widget(liked_songs)

        mycursor.execute(
            "select song_list.song, song_list.song_img, playlist.play from playlist inner join "
            "song_list where playlist.play_id=song_list.play_id AND song in (select * from played_songs) AND emotion ='sad';")
        res = mycursor.fetchall()
        for i in range(len(res)):
            img1 = ImageLeftWidget(source="songs/sad_songs/" + res[i][1])
            img2 = IconRightWidget(icon="heart", theme_text_color="Custom",
                                   text_color=[1, 1, 1, 1], on_release=self.add_to_liked_songs)
            if res[i][0] in fav_songs:
                img2.theme_text_color = "Custom"
                img2.text_color = [1, 0, 0, 1]
            liked_songs = TwoLineAvatarIconListItem(text="" + res[i][0], font_style="Subtitle1",
                                                    secondary_text=" " + res[i][2], secondary_font_style="Caption",
                                                    on_release=self.play)
            img3 = IconRightWidget(icon="play", padding=20, on_release=self.fav)
            liked_songs.add_widget(img1)
            liked_songs.add_widget(img2)
            liked_songs.add_widget(img3)
            self.root.ids.sad.add_widget(liked_songs)

        mycursor.execute(
            "select song_list.song, song_list.song_img, playlist.play from playlist inner join "
            "song_list where playlist.play_id=song_list.play_id AND song in (select * from played_songs) AND emotion ='fear';")
        res = mycursor.fetchall()
        for i in range(len(res)):
            img1 = ImageLeftWidget(source="songs/fear_songs/" + res[i][1])
            img2 = IconRightWidget(icon="heart", theme_text_color="Custom",
                                   text_color=[1, 1, 1, 1], on_release=self.add_to_liked_songs)
            if res[i][0] in fav_songs:
                img2.theme_text_color = "Custom"
                img2.text_color = [1, 0, 0, 1]
            liked_songs = TwoLineAvatarIconListItem(text="" + res[i][0], font_style="Subtitle1",
                                                    secondary_text=" " + res[i][2], secondary_font_style="Caption",
                                                    on_release=self.play)
            img3 = IconRightWidget(icon="play", padding=20, on_release=self.fav)
            liked_songs.add_widget(img1)
            liked_songs.add_widget(img2)
            liked_songs.add_widget(img3)
            self.root.ids.fear.add_widget(liked_songs)

        mycursor.execute(
            "select song_list.song, song_list.song_img, playlist.play from playlist inner join "
            "song_list where playlist.play_id=song_list.play_id AND song in (select * from played_songs) AND emotion ='disgust';")
        res = mycursor.fetchall()
        for i in range(len(res)):
            img1 = ImageLeftWidget(source="songs/disgust_songs/" + res[i][1])
            img2 = IconRightWidget(icon="heart", theme_text_color="Custom",
                                   text_color=[1, 1, 1, 1], on_release=self.add_to_liked_songs)
            if res[i][0] in fav_songs:
                img2.theme_text_color = "Custom"
                img2.text_color = [1, 0, 0, 1]
            liked_songs = TwoLineAvatarIconListItem(text="" + res[i][0], font_style="Subtitle1",
                                                    secondary_text=" " + res[i][2], secondary_font_style="Caption",
                                                    on_release=self.play)
            img3 = IconRightWidget(icon="play", padding=20, on_release=self.fav)
            liked_songs.add_widget(img1)
            liked_songs.add_widget(img2)
            liked_songs.add_widget(img3)
            self.root.ids.disgust.add_widget(liked_songs)

        mycursor.execute(
            "select song_list.song, song_list.song_img, playlist.play from playlist inner join "
            "song_list where playlist.play_id=song_list.play_id AND song in (select * from played_songs) AND emotion ='surprise';")
        res = mycursor.fetchall()
        for i in range(len(res)):
            img1 = ImageLeftWidget(source="songs/surprise_songs/" + res[i][1])
            img2 = IconRightWidget(icon="heart", theme_text_color="Custom",
                                   text_color=[1, 1, 1, 1], on_release=self.add_to_liked_songs)
            if res[i][0] in fav_songs:
                img2.theme_text_color = "Custom"
                img2.text_color = [1, 0, 0, 1]
            liked_songs = TwoLineAvatarIconListItem(text="" + res[i][0], font_style="Subtitle1",
                                                    secondary_text=" " + res[i][2], secondary_font_style="Caption",
                                                    on_release=self.play)
            img3 = IconRightWidget(icon="play", padding=20, on_release=self.fav)
            liked_songs.add_widget(img1)
            liked_songs.add_widget(img2)
            liked_songs.add_widget(img3)
            self.root.ids.surprise.add_widget(liked_songs)

        mycursor.execute(
            "select song_list.song, song_list.song_img, playlist.play from playlist inner join "
            "song_list where playlist.play_id=song_list.play_id AND song in (select * from played_songs) AND emotion ='angry';")
        res = mycursor.fetchall()
        for i in range(len(res)):
            img1 = ImageLeftWidget(source="songs/angry_songs/" + res[i][1])
            img2 = IconRightWidget(icon="heart", theme_text_color="Custom",
                                   text_color=[1, 1, 1, 1], on_release=self.add_to_liked_songs)
            if res[i][0] in fav_songs:
                img2.theme_text_color = "Custom"
                img2.text_color = [1, 0, 0, 1]
            liked_songs = TwoLineAvatarIconListItem(text="" + res[i][0], font_style="Subtitle1",
                                                    secondary_text=" " + res[i][2], secondary_font_style="Caption",
                                                    on_release=self.play)
            img3 = IconRightWidget(icon="play", padding=20, on_release=self.fav)
            liked_songs.add_widget(img1)
            liked_songs.add_widget(img2)
            liked_songs.add_widget(img3)
            self.root.ids.angry.add_widget(liked_songs)

# --------------------------------------------------------------------------------------------------------------------
# Run the App

DemoApp().run()