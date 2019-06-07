#!/usr/bin/env python3


"""
Author:
    Jay MacKilcline
Date:
    06/05/19
Description:
    Linux desktop app to take numerical values from a user
    and convert them into a color value.  Also, display the
    color value to the screen.
Associated Files:
    KV: colorpreview.kv
    Ico:
    App Ico:favico.png
"""

# Imports-----------------------------------------------------


import kivy
kivy.require('1.11.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


# Debug Function----------------------------------------------


"""
Debug:
    Debug function will be used to print various stages of 
    the program and its progress.  Used for testing and 
    debug.  Do not delete, annotate out if desired.
"""


def debug(x):
    print("Debug: " + str(x))


debug("Program Started")


# Root Widget-------------------------------------------------


"""
Root Widget:
    class-
    The root widget of the kv file has been passed.  In 
    this class, I am creating variables, and passing the
    arbitrary default values, so as to manipulate them in
    the functions.
    All of the corresponding ids from the kv file will
    be assigned in a function called :
    assign_imports_from_kv()    
"""


class RootWidget(GridLayout):
    color_value_one_text = int(0)
    color_value_two_text = int(0)
    color_value_three_text = int(0)
    color_value_alpha_text = float(1)
    new_color = (1, 1, 1, 1)

    """
    Assign values:
        The purpose of this function is to take all
        of the arbitrary values created in the class
        above, and link them to the ids in the kv 
        file.
    """

    def assign_imports_from_kv(self):
        RootWidget.color_value_one_text = self.color_value_one_text_root_kv.text
        RootWidget.color_value_two_text = self.color_value_two_text_root_kv.text
        RootWidget.color_value_three_text = self.color_value_three_text_root_kv.text
        RootWidget.color_value_alpha_text = self.color_value_alpha_text_root_kv.text
        RootWidget.new_color = (1, 1, 1, 1)

    """
    Change function:
        This is the function that will be called
        to take all of the values that were passed
        by the user in the TextInput fields, and 
        assign them to a new variable.
        The new variable will then be used to change 
        the background color of the button.
    """

    def change(self):
        RootWidget.new_color = (1, 1, 1, 1)
        RootWidget.assign_imports_from_kv(self)

        def try_change():
            returned_color = int(RootWidget.color_value_one_text), \
                int(RootWidget.color_value_two_text), \
                int(RootWidget.color_value_three_text), \
                float(RootWidget.color_value_alpha_text)
            RootWidget.new_color = returned_color
            return RootWidget.new_color

        """
        Try block:
            The try_change function is then put 
            inside a try-catch block in order to 
            catch any errors that may crash the 
            program.
        """

        try:
            try_change()
        except:
            debug("They entered a Letter")
        else:
            debug("nothing went wrong")
        finally:
            debug('try_change executed')

        debug("Inputs parsed to string")
        debug(RootWidget.new_color)
        self.display.background_color = RootWidget.new_color
        debug("Display background changed")
        """
        if Statement:
            This if statement places the focus of
            the cursor on the next avaliable TextInput
            field.  
            Without it, any change that is made to
            the TextInput field after the function
            is executed, would have no focus for the
            cursor.
        """
        if self.color_value_one_text_root_kv.focus == True:
            self.color_value_one_text_root_kv.focus = False
            self.color_value_two_text_root_kv.focus = True
        elif self.color_value_two_text_root_kv.focus == True:
            self.color_value_two_text_root_kv.focus = False
            self.color_value_three_text_root_kv.focus = True
        elif self.color_value_three_text_root_kv.focus == True:
            self.color_value_three_text_root_kv.focus = False
            self.color_value_alpha_text_root_kv.focus = True
        elif self.color_value_alpha_text_root_kv.focus == True:
            self.color_value_alpha_text_root_kv.focus = False
            self.color_value_one_text_root_kv.focus = True

# Main Method----------------------------------


class ColorPreviewApp(App):

    # Constructor------------------------------
    def build(self):
        # Change the window size
        Window.size = (350, 600)
        # Change the title of the window
        self.title = "Color Preview"
        return RootWidget()


debug("End of Main")
# Assign the main method to a variable.
color_preview_app = ColorPreviewApp()
# Call the run function on the variable.
color_preview_app.run()
