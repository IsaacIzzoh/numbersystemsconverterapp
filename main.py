# Number System Converter App
# This is a school assignment project that allows you to convert numbers between different number systems.
# The app is designed to run on Android devices.
#Developed and Designed by Kirinyaga University Students Digital Logic Group 2 
#Members
# 1. ISAAC GATHUA MURERE - CT100/G/15897/22
# 2. JOSEPH MWAURA MWARIRI - CT100/G/15893/22
# 3. JAMES MUITA - CT100/G/15929/22
# 4. RYAN WEKWSA SIMIYU - CT100/G/15984/22
# 5. ELIJAH MURAGE - CT100/S/20598/23
# copyright 2023 - Group 2
# Import KivyMD dependencies
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.gridlayout import GridLayout
from kivy.graphics.context_instructions import Color
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField  # Import MDTextField  
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.button import MDRoundFlatButton
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import AsyncImage
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDRectangleFlatButton

class NumberSystemConverterApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"

        self.screen_manager = ScreenManager()

        self.home_screen = HomeScreen(name='home')
        self.settings_screen = SettingsScreen(
            name='settings')
        self.decimal_to_binary_screen = DecimalToBinaryScreen(
            name='decimal_to_binary')

        self.binary_to_octal_screen = BinaryToOctalScreen(
            name='binary_to_octal')

        self.binary_to_hexadecimal_screen = BinaryToHexScreen(
            name='binary_to_hexadecimal')
        
        self.binary_to_decimal_screen = BinaryToDecimalScreen(
            name='binary_to_decimal')
        
        self.octal_to_binary_screen = OctalToBinaryScreen(
            name='octal_to_binary')
        
        self.hexadecimal_to_binary_screen = HexadecimalToBinaryScreen(
            name='hexadecimal_to_binary')
        
        self.decimal_to_octal_screen = DecimalToOctalScreen(
            name='decimal_to_octal')
        
        self.octal_to_decimal_screen = OctalToDecimalScreen(
            name='octal_to_decimal')
        
        self.hexadecimal_to_octal_screen = HexadecimalToOctalScreen(
            name='hexadecimal_to_octal')
        
        self.decimal_to_hexadecimal_screen = DecimalToHexadecimalScreen(
            name='decimal_to_hexadecimal')
        
        self.octal_to_hexadecimal_screen = OctalToHexadecimalScreen(
            name='octal_to_hexadecimal')
        
        self.hexadecimal_to_decimal_screen = HexadecimalToDecimalScreen(
            name='hexadecimal_to_decimal')


        self.screen_manager.add_widget(self.home_screen)
        self.screen_manager.add_widget(self.settings_screen)
        self.screen_manager.add_widget(self.decimal_to_binary_screen)
        self.screen_manager.add_widget(self.binary_to_octal_screen)
        self.screen_manager.add_widget(self.binary_to_hexadecimal_screen)
        self.screen_manager.add_widget(self.binary_to_decimal_screen)
        self.screen_manager.add_widget(self.octal_to_binary_screen)
        self.screen_manager.add_widget(self.hexadecimal_to_binary_screen)
        self.screen_manager.add_widget(self.decimal_to_octal_screen)
        self.screen_manager.add_widget(self.octal_to_decimal_screen)
        self.screen_manager.add_widget(self.hexadecimal_to_octal_screen)
        self.screen_manager.add_widget(self.decimal_to_hexadecimal_screen)
        self.screen_manager.add_widget(self.octal_to_hexadecimal_screen)
        self.screen_manager.add_widget(self.hexadecimal_to_decimal_screen)

        self.layout = MDBoxLayout(orientation="vertical")
        

       
        self.layout.add_widget(self.screen_manager)

        self.confirmation_dialog = MDDialog(
            title="Exit App",
            text="Do you really want to exit the app?",
            buttons=[
                MDRoundFlatButton(
                    text="Cancel", on_release=self.close_confirmation_dialog
                ),
                MDFillRoundFlatButton(
                    text="Exit", on_release=self.exit_app
                ),
            ],
        )

        Window.bind(on_keyboard=self.on_key_down)

        return self.layout

    def on_key_down(self, window, key, scancode, codepoint, modifier):
        # Override the default behavior for the "Escape" key
        if key == 27:  # 27 is the key code for the "Escape" key
            current_screen_name = self.screen_manager.current
            if current_screen_name == 'home':
                # Show confirmation dialog on home screen
                self.confirmation_dialog.open()
                return True  # Prevent default behavior

            elif current_screen_name != 'home':
                # Switch to the 'home' screen
                self.screen_manager.current = 'home'
                return True  # Prevent default behavior

        return False  # Continue with default behavior
    def close_confirmation_dialog(self, instance):
        self.confirmation_dialog.dismiss()

    def exit_app(self, instance):
        self.confirmation_dialog.dismiss()
        self.stop()

# Header Class
    

class RippleButton(MDFillRoundFlatButton, ButtonBehavior):
    pass
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        # Create a BoxLayout to arrange the content vertically
        content_layout = BoxLayout(orientation='vertical', spacing=0)

        # Create a header with a green background color
        header = BoxLayout(orientation='horizontal', size_hint=(1, None), height="48dp")
        with header.canvas:
            Color(0.0, 0.5, 0.5, 0.7)  # Teal color (RGBA)
            self.rect = Rectangle(pos=header.pos, size=header.size)

        # Update the background when the position or size changes
        header.bind(pos=self.update_rect, size=self.update_rect)

        self.y_button = MDIconButton(icon="")
        # Create a title label
        self.title_label = MDLabel(text="Number Systems Converter", halign="center", valign="middle", theme_text_color="Secondary")

        # Create a settings button with a click event to open the Settings screen
        self.settings_button = MDIconButton(icon="information-outline", theme_text_color="Secondary")
        self.settings_button.bind(on_release=self.open_settings_screen)

        # Add widgets to the header
        header.add_widget(self.y_button)
        header.add_widget(self.title_label)
        header.add_widget(self.settings_button)
        

        # Add the header to the content layout
        content_layout.add_widget(header)

        # Create a label for the title
        home_label = MDLabel(
            text="Welcome!! Enjoy Our App!",
            halign="center",
            font_style="H4",
        )

        content_layout.add_widget(home_label)

        # Create a grid layout for the buttons
        grid_layout = GridLayout(cols=2, spacing=dp(10), padding=dp(20))
        grid_layout.id = 'grid_layout'  # Assign an ID to the grid_layout

        # Buttons for various conversions and their reverses
        conversions = [
            ("Decimal to Binary", self.open_decimal_to_binary),
            ("Decimal to Octal", self.open_decimal_to_octal),
            ("Decimal to Hexadecimal", self.open_decimal_to_hexadecimal),
            ("Binary to Decimal", self.open_binary_to_decimal),
            ("Binary to Octal", self.open_binary_to_octal),
            ("Binary to Hexadecimal", self.open_binary_to_hexadecimal),
            ("Octal to Binary", self.open_octal_to_binary),
            ("Octal to Decimal", self.open_octal_to_decimal),
            ("Octal to Hexadecimal", self.open_octal_to_hexadecimal),
            ("Hexadecimal to Binary", self.open_hexadecimal_to_binary),
            ("Hexadecimal to Decimal", self.open_hexadecimal_to_decimal),
            ("Hexadecimal to Octal", self.open_hexadecimal_to_octal),
        ]

        # Create buttons and add them to the grid layout
        for text, callback in conversions:
            button = MDFillRoundFlatButton(text=text, on_release=callback)
            grid_layout.add_widget(button)

        # Create a ScrollView to handle scrolling on smaller screens
        scroll_view = ScrollView()
        scroll_view.add_widget(grid_layout)

        # Store a reference to the grid layout as an instance variable
        self.grid_layout = grid_layout

        # Add the ScrollView to the content layout
        content_layout.add_widget(scroll_view)

        # Add the content layout to the screen
        self.add_widget(content_layout)

    def open_decimal_to_binary(self, instance):
        self.manager.current = "decimal_to_binary"

    def open_decimal_to_octal(self, instance):
        self.manager.current = "decimal_to_octal"

    def open_decimal_to_hexadecimal(self, instance):
        self.manager.current = "decimal_to_hexadecimal"

    def open_binary_to_decimal(self, instance):
        self.manager.current = "binary_to_decimal"

    def open_binary_to_octal(self, instance):
        self.manager.current = "binary_to_octal"

    def open_binary_to_hexadecimal(self, instance):
        self.manager.current = "binary_to_hexadecimal"

    def open_octal_to_binary(self, instance):
        self.manager.current = "octal_to_binary"

    def open_octal_to_decimal(self, instance):
        self.manager.current = "octal_to_decimal"

    def open_octal_to_hexadecimal(self, instance):
        self.manager.current = "octal_to_hexadecimal"

    def open_hexadecimal_to_binary(self, instance):
        self.manager.current = "hexadecimal_to_binary"

    def open_hexadecimal_to_decimal(self, instance):
        self.manager.current = "hexadecimal_to_decimal"

    def open_hexadecimal_to_octal(self, instance):
        self.manager.current = "hexadecimal_to_octal"

    def open_settings_screen(self, instance):
        # Open the Settings screen
        self.manager.current = "settings"

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

# class for decimal to binary
class DecimalToBinaryScreen(Screen):
    def __init__(self, **kwargs):
        super(DecimalToBinaryScreen, self).__init__(**kwargs)

        # Create a BoxLayout to center the content below the header
        content_layout = MDBoxLayout(orientation="vertical", padding=0, spacing=0)

        # Create a header with a green background color
        header = MDBoxLayout(orientation='horizontal', size_hint=(1, None), height="48dp")
        with header.canvas:
            Color(0.0, 0.5, 0.5, 0.7)  # Teal color (RGBA)
            self.rect = Rectangle(pos=header.pos, size=header.size)

        # Update the background when the position or size changes
        header.bind(pos=self.update_rect, size=self.update_rect)

        # Create a back button
        self.back_button = MDIconButton(icon="arrow-left", on_release=self.back, theme_text_color="Secondary")

        # Create a title label
        self.title_label = MDLabel(text="Decimal To Binary Conversion", halign="center", valign="middle", theme_text_color="Secondary")

        # Add widgets to the header
        header.add_widget(self.back_button)
        header.add_widget(self.title_label)

        # Add the header to the content layout
        content_layout.add_widget(header)

        body = MDBoxLayout(orientation="vertical", padding=60, spacing=20)
        self.input_text = MDTextField(hint_text="Enter a decimal number")
        self.convert_button = MDFillRoundFlatButton(
            text="Convert", on_release=self.convert)
        self.clear_button = MDRoundFlatButton(
            text="Clear", on_release=self.clear)
        self.output_label = MDLabel(text="Binary equivalent:", halign="center")
        self.output_text = MDTextField(readonly=True)

        self.convert_button.bind(on_release=self.convert)

        # Add the input and output elements to the content layout
        body.add_widget(self.input_text)
        body.add_widget(self.convert_button)
        body.add_widget(self.clear_button)
        body.add_widget(self.output_label)
        body.add_widget(self.output_text)

        # Add the body to the content layout
        content_layout.add_widget(body)
        self.add_widget(content_layout)


    
    def convert(self, instance):
        decimal_input = self.input_text.text
        try:
            decimal_input = float(decimal_input)
            binary_output = self.dec_bin(decimal_input)
            self.output_text.text = binary_output
        except ValueError:
            self.output_text.text = 'Invalid Input'

    def dec_bin(self, num):
        num = str(num).strip()
        integer = ''
        decimal = ''
        bin_num = ''
        temp_bin = ''
        flagdec = False

        for i in num:
            if i == '.' and not flagdec:
                flagdec = True
            elif (not i.isdigit() and i != '.') or (i == '.' and flagdec):
                return 'Wrong Input. Please check the input again.'

        for i in range(len(num)):
            if num[i] == '.':
                decimal = '0.' + num[i + 1:]
                break
            integer += num[i]

        if not integer:
            integer = 0
        else:
            integer = int(integer)

        while integer > 0:
            temp = integer % 2
            bin_num = str(temp) + bin_num
            integer = integer // 2

        if not bin_num:
            bin_num = '0'

        decimal = float(decimal)
        for i in range(4):
            decimal *= 2
            temp = int(decimal)
            decimal -= temp
            temp_bin += str(temp)

        temp_bin = temp_bin.rstrip('0')

        if not temp_bin:
            temp_bin = '0'

        bin_num = bin_num + '.' + temp_bin
        return bin_num
    def clear(self, instance):
        self.input_text.text = ""
        self.output_text.text = ""
    

    def back(self, instance):
        self.manager.current = "home"

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class BinaryToOctalScreen(Screen):
    def __init__(self, **kwargs):
        super(BinaryToOctalScreen, self).__init__(**kwargs)

        # Create a BoxLayout to center the content below the header
        content_layout = MDBoxLayout(orientation="vertical", padding=0, spacing=0)

        # Create a header with a green background color
        header = MDBoxLayout(orientation='horizontal', size_hint=(1, None), height="48dp")
        with header.canvas:
            Color(0.0, 0.5, 0.5, 0.7)  # Teal color (RGBA)
            self.rect = Rectangle(pos=header.pos, size=header.size)

        # Update the background when the position or size changes
        header.bind(pos=self.update_rect, size=self.update_rect)

        # Create a back button
        self.back_button = MDIconButton(icon="arrow-left", on_release=self.back, theme_text_color="Secondary")

        # Create a title label
        self.title_label = MDLabel(text="Binary To Octal Conversion", halign="center", valign="middle", theme_text_color="Secondary")

        # Add widgets to the header
        header.add_widget(self.back_button)
        header.add_widget(self.title_label)

        # Add the header to the content layout
        content_layout.add_widget(header)
        
        body = MDBoxLayout(orientation="vertical", padding=60, spacing=20)

        

        self.input_text = MDTextField(hint_text="Enter a Binary number")
        self.convert_button = MDFillRoundFlatButton(text="Convert")
        self.convert_button.bind(on_release=self.convert)
        self.clear_button = MDRoundFlatButton(
            text="Clear", on_release=self.clear)
        self.output_label = MDLabel(text="Octal equivalent:", halign="center")
        self.output_text = MDTextField(readonly=True)

        body.add_widget(self.input_text)
        body.add_widget(self.convert_button)
        body.add_widget(self.clear_button)
        body.add_widget(self.output_label)
        body.add_widget(self.output_text)

        # Add the body to the content layout
        content_layout.add_widget(body)
        self.add_widget(content_layout)

    def convert(self, instance):
        binary_input = self.input_text.text
        try:
            octal_output = self.bin_oct(binary_input)
            self.output_text.text = octal_output
        except ValueError:
            self.output_text.text = 'Invalid Input'

    def bin_oct(self, num):
        num = str(num).strip()
        octal = ''
        flagbin = False
        integer = ''
        decimal = ''

        NumMap = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'}

        for i in num:
            if i == '.' and flagbin == False:
                flagbin = True
            elif ((i not in ('0', '1')) and i != '.') or (i == '.' and flagbin == True):
                raise ValueError('Wrong Input. Please check the input again.')

        for i in range(len(num)):
            if num[i] == '.':
                decimal = num[i+1:]
                break
            integer += num[i]

        if decimal == '':
            decimal = '0'

        end_marker = len(integer)
        begining_marker = len(integer)

        while end_marker > 0:
            begining_marker -= 3
            if begining_marker < 0:
                begining_marker = 0
            sliced = num[begining_marker:end_marker]
            while len(sliced) < 3:
                sliced = '0' + sliced
            octal = NumMap[sliced] + octal
            end_marker = begining_marker

        octal = octal.lstrip('0')
        if octal == '':
            octal = '0'

        octal = octal + '.'

        end_marker = 0
        begining_marker = 0
        dec_len = len(decimal)

        while begining_marker < dec_len:
            end_marker += 3
            if begining_marker > dec_len:
                begining_marker = dec_len
            sliced = decimal[begining_marker:end_marker]
            while len(sliced) < 3:
                sliced = sliced + '0'
            octal = octal + NumMap[sliced]
            begining_marker = end_marker

        return octal
    
    def clear(self, instance):
        self.input_text.text = ""
        self.output_text.text = ""
    

    def back(self, instance):
        self.manager.current = "home"

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
#screen for binary to hexadecimal
class BinaryToHexScreen(Screen):
    def __init__(self, **kwargs):
        super(BinaryToHexScreen, self).__init__(**kwargs)
        
        # Create a BoxLayout to center the content below the header
        content_layout = MDBoxLayout(orientation="vertical", padding=0, spacing=0)

        # Create a header with a green background color
        header = MDBoxLayout(orientation='horizontal', size_hint=(1, None), height="48dp")
        with header.canvas:
            Color(0.0, 0.5, 0.5, 0.7)  # Teal color (RGBA)
            self.rect = Rectangle(pos=header.pos, size=header.size)

        # Update the background when the position or size changes
        header.bind(pos=self.update_rect, size=self.update_rect)

        # Create a back button
        self.back_button = MDIconButton(icon="arrow-left", on_release=self.back, theme_text_color="Secondary")

        # Create a title label
        self.title_label = MDLabel(text="Binary To HexaDecimal Conversion", halign="center", valign="middle", theme_text_color="Secondary")

        # Add widgets to the header
        header.add_widget(self.back_button)
        header.add_widget(self.title_label)

        # Add the header to the content layout
        content_layout.add_widget(header)
        
        body = MDBoxLayout(orientation="vertical", padding=60, spacing=20)

        

        self.input_text = MDTextField(hint_text="Enter a Binary number")
        self.convert_button = MDFillRoundFlatButton(text="Convert")
        self.convert_button.bind(on_release=self.convert)
        self.clear_button = MDRoundFlatButton(
            text="Clear", on_release=self.clear)
        self.output_label = MDLabel(text="Hexadecimal equivalent:", halign="center")
        self.output_text = MDTextField(readonly=True)

        body.add_widget(self.input_text)
        body.add_widget(self.convert_button)
        body.add_widget(self.clear_button)
        body.add_widget(self.output_label)
        body.add_widget(self.output_text)

        # Add the body to the content layout
        content_layout.add_widget(body)
        self.add_widget(content_layout)

    def convert(self, instance):
        binary_input = self.input_text.text
        try:
            hexadecimal_output = self.bin_hex(binary_input)
            self.output_text.text = hexadecimal_output
        except ValueError:
            self.output_text.text = 'Invalid Input'

    def bin_hex(self, num):
        num = str(num).strip()
        hexadecimal = ''
        flagbin = False
        integer = ''
        decimal = ''

        NumMap = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                  '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

        for i in num:
            if i == '.' and flagbin == False:
                flagbin = True
            elif ((i not in ('0', '1')) and i != '.') or (i == '.' and flagbin == True):
                raise ValueError('Wrong Input. Please check the input again.')

        for i in range(len(num)):
            if num[i] == '.':
                decimal = num[i+1:]
                break
            integer += num[i]

        if decimal == '':
            decimal = '0'

        end_marker = len(integer)
        begining_marker = len(integer)

        while end_marker > 0:
            begining_marker -= 4
            if begining_marker < 0:
                begining_marker = 0
            sliced = num[begining_marker:end_marker]
            while len(sliced) < 4:
                sliced = '0' + sliced
            hexadecimal = NumMap[sliced] + hexadecimal
            end_marker = begining_marker

        hexadecimal = hexadecimal.lstrip('0')
        if hexadecimal == '':
            hexadecimal = '0'

        hexadecimal = hexadecimal + '.'

        end_marker = 0
        begining_marker = 0
        dec_len = len(decimal)

        while begining_marker < dec_len:
            end_marker += 4
            if begining_marker > dec_len:
                begining_marker = dec_len
            sliced = decimal[begining_marker:end_marker]
            while len(sliced) < 4:
                sliced = sliced + '0'
            hexadecimal = hexadecimal + NumMap[sliced]
            begining_marker = end_marker

        return hexadecimal

    def clear(self, instance):
        self.input_text.text = ""
        self.output_text.text = ""
    

    def back(self, instance):
        self.manager.current = "home"

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
#binary to decimal
class BinaryToDecimalScreen(Screen):
    def __init__(self, **kwargs):
        super(BinaryToDecimalScreen, self).__init__(**kwargs)
        
        # Create a BoxLayout to center the content below the header
        content_layout = MDBoxLayout(orientation="vertical", padding=0, spacing=0)

        # Create a header with a green background color
        header = MDBoxLayout(orientation='horizontal', size_hint=(1, None), height="48dp")
        with header.canvas:
            Color(0.0, 0.5, 0.5, 0.7)  # Teal color (RGBA)
            self.rect = Rectangle(pos=header.pos, size=header.size)

        # Update the background when the position or size changes
        header.bind(pos=self.update_rect, size=self.update_rect)

        # Create a back button
        self.back_button = MDIconButton(icon="arrow-left", on_release=self.back, theme_text_color="Secondary")

        # Create a title label
        self.title_label = MDLabel(text="Binary To Decimal Conversion", halign="center", valign="middle", theme_text_color="Secondary")

        # Add widgets to the header
        header.add_widget(self.back_button)
        header.add_widget(self.title_label)

        # Add the header to the content layout
        content_layout.add_widget(header)
        
        body = MDBoxLayout(orientation="vertical", padding=60, spacing=20)

        

        self.input_text = MDTextField(hint_text="Enter a Binary number")
        self.convert_button = MDFillRoundFlatButton(text="Convert")
        self.convert_button.bind(on_release=self.convert)
        self.clear_button = MDRoundFlatButton(
            text="Clear", on_release=self.clear)
        self.output_label = MDLabel(text="Decimal equivalent:", halign="center")
        self.output_text = MDTextField(readonly=True)

        body.add_widget(self.input_text)
        body.add_widget(self.convert_button)
        body.add_widget(self.clear_button)
        body.add_widget(self.output_label)
        body.add_widget(self.output_text)

        # Add the body to the content layout
        content_layout.add_widget(body)
        self.add_widget(content_layout)

    def convert(self, instance):
        binary_input = self.input_text.text
        try:
            decimal_output = self.bin_dec(binary_input)
            self.output_text.text = decimal_output
        except ValueError:
            self.output_text.text = 'Invalid Input'

    def bin_dec(self, num):
        num = str(num).strip()
        decimal = 0
        flagbin = False
        integer = ''
        decimal_part = ''

        for i in num:
            if i == '.' and flagbin is False:
                flagbin = True
            elif ((i not in ('0', '1')) and i != '.') or (i == '.' and flagbin is True):
                raise ValueError('Wrong Input. Please check the input again.')

        for i in range(len(num)):
            if num[i] == '.':
                decimal_part = num[i + 1:]
                break
            integer += num[i]

        if decimal_part == '':
            decimal_part = '0'

        integer = integer[::-1]  # Reverse the integer part to start from the right

        for i in range(len(integer)):
            decimal += int(integer[i]) * (2 ** i)

        for i in range(len(decimal_part)):
            decimal += int(decimal_part[i]) * (2 ** (-i - 1))

        return str(decimal)

    def clear(self, instance):
        self.input_text.text = ""
        self.output_text.text = ""
    

    def back(self, instance):
        self.manager.current = "home"

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
class OctalToBinaryScreen(Screen):
    def __init__(self, **kwargs):
        super(OctalToBinaryScreen, self).__init__(**kwargs)
        
        # Create a BoxLayout to center the content below the header
        content_layout = MDBoxLayout(orientation="vertical", padding=0, spacing=0)

        # Create a header with a green background color
        header = MDBoxLayout(orientation='horizontal', size_hint=(1, None), height="48dp")
        with header.canvas:
            Color(0.0, 0.5, 0.5, 0.7)  # Teal color (RGBA)
            self.rect = Rectangle(pos=header.pos, size=header.size)

        # Update the background when the position or size changes
        header.bind(pos=self.update_rect, size=self.update_rect)

        # Create a back button
        self.back_button = MDIconButton(icon="arrow-left", on_release=self.back, theme_text_color="Secondary")

        # Create a title label
        self.title_label = MDLabel(text="Octal To Binary Conversion", halign="center", valign="middle", theme_text_color="Secondary")

        # Add widgets to the header
        header.add_widget(self.back_button)
        header.add_widget(self.title_label)

        # Add the header to the content layout
        content_layout.add_widget(header)
        
        body = MDBoxLayout(orientation="vertical", padding=60, spacing=20)
        self.layout = BoxLayout(orientation="vertical", padding=60, spacing=20)

        self.input_text = MDTextField(hint_text="Enter an Octal number")
        self.convert_button = MDFillRoundFlatButton(text="Convert")
        self.convert_button.bind(on_press=self.convert)
        self.clear_button = MDRoundFlatButton(
            text="Clear", on_release=self.clear)
        self.output_label = MDLabel(text="Binary equivalent:", halign="center")
        self.output_text = MDTextField(readonly=True)

        body.add_widget(self.input_text)
        body.add_widget(self.convert_button)
        body.add_widget(self.clear_button)
        body.add_widget(self.output_label)
        body.add_widget(self.output_text)

        # Add the body to the content layout
        content_layout.add_widget(body)
        self.add_widget(content_layout)

    def convert(self, instance):
        octal_input = self.input_text.text
        try:
            binary_output = self.oct_to_bin(octal_input)
            self.output_text.text = binary_output
        except ValueError:
            self.output_text.text = 'Invalid Input'

    def oct_to_bin(self, num):
        try:
            num = int(num, 8) 
             # Convert the octal input to an integer
        except ValueError:
            raise ValueError
        

        if num < 0:
            raise ValueError("Octal input must be non-negative")

        binary = bin(num)[2:]  # Convert the integer to binary and remove the '0b' prefix
        return binary

    def clear(self, instance):
        self.input_text.text = ""
        self.output_text.text = ""
    

    def back(self, instance):
        self.manager.current = "home"

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
class HexadecimalToBinaryScreen(Screen):
    def __init__(self, **kwargs):
        super(HexadecimalToBinaryScreen, self).__init__(**kwargs)
        
        # Create a BoxLayout to center the content below the header
        content_layout = MDBoxLayout(orientation="vertical", padding=0, spacing=0)

        # Create a header with a green background color
        header = MDBoxLayout(orientation='horizontal', size_hint=(1, None), height="48dp")
        with header.canvas:
            Color(0.0, 0.5, 0.5, 0.7)  # Teal color (RGBA)
            self.rect = Rectangle(pos=header.pos, size=header.size)

        # Update the background when the position or size changes
        header.bind(pos=self.update_rect, size=self.update_rect)

        # Create a back button
        self.back_button = MDIconButton(icon="arrow-left", on_release=self.back, theme_text_color="Secondary")

        # Create a title label
        self.title_label = MDLabel(text="Hexadecimal To Binary Conversion", halign="center", valign="middle", theme_text_color="Secondary")

        # Add widgets to the header
        header.add_widget(self.back_button)
        header.add_widget(self.title_label)

        # Add the header to the content layout
        content_layout.add_widget(header)
        
        body = MDBoxLayout(orientation="vertical", padding=60, spacing=20)

        

        self.input_text = MDTextField(hint_text="Enter a Hexadecimal number")
        self.convert_button = MDFillRoundFlatButton(text="Convert")
        self.convert_button.bind(on_release=self.convert)
        self.clear_button = MDRoundFlatButton(
            text="Clear", on_release=self.clear)
        self.output_label = MDLabel(text="Binary equivalent:", halign="center")
        self.output_text = MDTextField(readonly=True)

        body.add_widget(self.input_text)
        body.add_widget(self.convert_button)
        body.add_widget(self.clear_button)
        body.add_widget(self.output_label)
        body.add_widget(self.output_text)

        # Add the body to the content layout
        content_layout.add_widget(body)
        self.add_widget(content_layout)

    def convert(self, instance):
        hexadecimal_input = self.input_text.text
        try:
            binary_output = self.hex_to_bin(hexadecimal_input)
            self.output_text.text = binary_output
        except ValueError:
            self.output_text.text = 'Invalid Input'

    def hex_to_bin(self, num):
        num = num.strip()  # Remove leading/trailing spaces
        num = num.upper()  # Convert to uppercase for consistency

        if not all(c in '0123456789ABCDEF.' for c in num):
            raise ValueError('Invalid Input')

        binary = ''
        flagdec = False

        NumMap = {
            '0': '0000', '1': '0001', '2': '0010', '3': '0011',
            '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
            'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
        }

        for char in num:
            if char == '.':
                if flagdec:
                    raise ValueError('Wrong Input. Please check the input again.')
                flagdec = True
                binary += '.'
            else:
                binary += NumMap[char]

        return binary.lstrip('0').rstrip('.')

    def clear(self, instance):
        self.input_text.text = ""
        self.output_text.text = ""
    

    def back(self, instance):
        self.manager.current = "home"

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
#decimal to octal screen
class DecimalToOctalScreen(Screen):
    def __init__(self, **kwargs):
        super(DecimalToOctalScreen, self).__init__(**kwargs)
        
        # Create a BoxLayout to center the content below the header
        content_layout = MDBoxLayout(orientation="vertical", padding=0, spacing=0)

        # Create a header with a green background color
        header = MDBoxLayout(orientation='horizontal', size_hint=(1, None), height="48dp")
        with header.canvas:
            Color(0.0, 0.5, 0.5, 0.7)  # Teal color (RGBA)
            self.rect = Rectangle(pos=header.pos, size=header.size)

        # Update the background when the position or size changes
        header.bind(pos=self.update_rect, size=self.update_rect)

        # Create a back button
        self.back_button = MDIconButton(icon="arrow-left", on_release=self.back, theme_text_color="Secondary")

        # Create a title label
        self.title_label = MDLabel(text="Decimal To Octal Conversion", halign="center", valign="middle", theme_text_color="Secondary")

        # Add widgets to the header
        header.add_widget(self.back_button)
        header.add_widget(self.title_label)

        # Add the header to the content layout
        content_layout.add_widget(header)
        
        body = MDBoxLayout(orientation="vertical", padding=60, spacing=20)

        

        self.input_text = MDTextField(hint_text="Enter a Decimal number")
        self.convert_button = MDFillRoundFlatButton(text="Convert")
        self.convert_button.bind(on_release=self.convert)
        self.clear_button = MDRoundFlatButton(
            text="Clear", on_release=self.clear)
        self.output_label = MDLabel(text="Octal equivalent:", halign="center")
        self.output_text = MDTextField(readonly=True)

        body.add_widget(self.input_text)
        body.add_widget(self.convert_button)
        body.add_widget(self.clear_button)
        body.add_widget(self.output_label)
        body.add_widget(self.output_text)

        # Add the body to the content layout
        content_layout.add_widget(body)
        self.add_widget(content_layout)

    def convert(self, instance):
        decimal_input = self.input_text.text
        try:
            octal_output = self.decimal_to_octal(decimal_input)
            self.output_text.text = octal_output
        except ValueError:
            self.output_text.text = 'Invalid Input'

    def decimal_to_octal(self, num):
        try:
            decimal_num = int(num)
            octal = oct(decimal_num).replace("0o", "")
            return octal
        except ValueError:
            raise ValueError('Invalid Input. Please check the input and try again')
    
    def clear(self, instance):
        self.input_text.text = ""
        self.output_text.text = ""
    

    def back(self, instance):
        self.manager.current = "home"

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        
#octal to decimal screen
class OctalToDecimalScreen(Screen):
    def __init__(self, **kwargs):
        super(OctalToDecimalScreen, self).__init__(**kwargs)
        
        # Create a BoxLayout to center the content below the header
        content_layout = MDBoxLayout(orientation="vertical", padding=0, spacing=0)

        # Create a header with a green background color
        header = MDBoxLayout(orientation='horizontal', size_hint=(1, None), height="48dp")
        with header.canvas:
            Color(0.0, 0.5, 0.5, 0.7)  # Teal color (RGBA)
            self.rect = Rectangle(pos=header.pos, size=header.size)

        # Update the background when the position or size changes
        header.bind(pos=self.update_rect, size=self.update_rect)

        # Create a back button
        self.back_button = MDIconButton(icon="arrow-left", on_release=self.back, theme_text_color="Secondary")

        # Create a title label
        self.title_label = MDLabel(text="Octal To Decimal Conversion", halign="center", valign="middle", theme_text_color="Secondary")

        # Add widgets to the header
        header.add_widget(self.back_button)
        header.add_widget(self.title_label)

        # Add the header to the content layout
        content_layout.add_widget(header)
        
        body = MDBoxLayout(orientation="vertical", padding=60, spacing=20)

        

        self.input_text = MDTextField(hint_text="Enter an Octal number")
        self.convert_button = MDFillRoundFlatButton(text="Convert")
        self.convert_button.bind(on_release=self.convert)
        self.clear_button = MDRoundFlatButton(
            text="Clear", on_release=self.clear)
        self.output_label = MDLabel(text="Decimal equivalent:", halign="center")
        self.output_text = MDTextField(readonly=True)

        body.add_widget(self.input_text)
        body.add_widget(self.convert_button)
        body.add_widget(self.clear_button)
        body.add_widget(self.output_label)
        body.add_widget(self.output_text)

        # Add the body to the content layout
        content_layout.add_widget(body)
        self.add_widget(content_layout)

    def convert(self, instance):
        octal_input = self.input_text.text
        try:
            decimal_output = self.octal_to_decimal(octal_input)
            self.output_text.text = decimal_output
        except ValueError:
            self.output_text.text = 'Invalid Input'

    def octal_to_decimal(self, num):
        try:
            decimal_num = int(num, 8)
            return str(decimal_num)
        except ValueError:
            raise ValueError('Invalid Input. Please check the input and try again')
    
    def clear(self, instance):
        self.input_text.text = ""
        self.output_text.text = ""
    

    def back(self, instance):
        self.manager.current = "home"

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

#hexadeciml to octal  
class HexadecimalToOctalScreen(Screen):
    def __init__(self, **kwargs):
        super(HexadecimalToOctalScreen, self).__init__(**kwargs)
        
        # Create a BoxLayout to center the content below the header
        content_layout = MDBoxLayout(orientation="vertical", padding=0, spacing=0)

        # Create a header with a green background color
        header = MDBoxLayout(orientation='horizontal', size_hint=(1, None), height="48dp")
        with header.canvas:
            Color(0.0, 0.5, 0.5, 0.7)  # Teal color (RGBA)
            self.rect = Rectangle(pos=header.pos, size=header.size)

        # Update the background when the position or size changes
        header.bind(pos=self.update_rect, size=self.update_rect)

        # Create a back button
        self.back_button = MDIconButton(icon="arrow-left", on_release=self.back, theme_text_color="Secondary")

        # Create a title label
        self.title_label = MDLabel(text="Hexadecimal To Octal Conversion", halign="center", valign="middle", theme_text_color="Secondary")

        # Add widgets to the header
        header.add_widget(self.back_button)
        header.add_widget(self.title_label)

        # Add the header to the content layout
        content_layout.add_widget(header)
        
        body = MDBoxLayout(orientation="vertical", padding=60, spacing=20)

        

        self.input_text = MDTextField(hint_text="Enter a Hexadecimal number")
        self.convert_button = MDFillRoundFlatButton(text="Convert")
        self.convert_button.bind(on_release=self.convert)
        self.clear_button = MDRoundFlatButton(
            text="Clear", on_release=self.clear)
        self.output_label = MDLabel(text="Octal equivalent:", halign="center")
        self.output_text = MDTextField(readonly=True)

        body.add_widget(self.input_text)
        body.add_widget(self.convert_button)
        body.add_widget(self.clear_button)
        body.add_widget(self.output_label)
        body.add_widget(self.output_text)

        # Add the body to the content layout
        content_layout.add_widget(body)
        self.add_widget(content_layout)

    def convert(self, instance):
        hexadecimal_input = self.input_text.text
        try:
            decimal_value = int(hexadecimal_input, 16)  # Convert hex to decimal
            octal_output = self.decimal_to_octal(decimal_value)
            self.output_text.text = octal_output
        except ValueError:
            self.output_text.text = 'Invalid Input'

    def decimal_to_octal(self, num):
        try:
            octal = oct(num).replace("0o", "")  # Convert decimal to octal
            return octal
        except ValueError:
            raise ValueError('Invalid Input. Please check the input and try again')
    
    def clear(self, instance):
        self.input_text.text = ""
        self.output_text.text = ""
    

    def back(self, instance):
        self.manager.current = "home"

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        
#decimal to hexadecimal
class DecimalToHexadecimalScreen(Screen):
    def __init__(self, **kwargs):
        super(DecimalToHexadecimalScreen, self).__init__(**kwargs)
        
        # Create a BoxLayout to center the content below the header
        content_layout = MDBoxLayout(orientation="vertical", padding=0, spacing=0)

        # Create a header with a green background color
        header = MDBoxLayout(orientation='horizontal', size_hint=(1, None), height="48dp")
        with header.canvas:
            Color(0.0, 0.5, 0.5, 0.7)  # Teal color (RGBA)
            self.rect = Rectangle(pos=header.pos, size=header.size)

        # Update the background when the position or size changes
        header.bind(pos=self.update_rect, size=self.update_rect)

        # Create a back button
        self.back_button = MDIconButton(icon="arrow-left", on_release=self.back, theme_text_color="Secondary")

        # Create a title label
        self.title_label = MDLabel(text="Decimal To Hexadecimal Conversion", halign="center", valign="middle", theme_text_color="Secondary")

        # Add widgets to the header
        header.add_widget(self.back_button)
        header.add_widget(self.title_label)

        # Add the header to the content layout
        content_layout.add_widget(header)
        
        body = MDBoxLayout(orientation="vertical", padding=60, spacing=20)

        

        self.input_text = MDTextField(hint_text="Enter a Decimal number")
        self.convert_button = MDFillRoundFlatButton(text="Convert")
        self.convert_button.bind(on_release=self.convert)
        self.clear_button = MDRoundFlatButton(
            text="Clear", on_release=self.clear)
        self.output_label = MDLabel(text="Hexadecimal equivalent:", halign="center")
        self.output_text = MDTextField(readonly=True)

        body.add_widget(self.input_text)
        body.add_widget(self.convert_button)
        body.add_widget(self.clear_button)
        body.add_widget(self.output_label)
        body.add_widget(self.output_text)

        # Add the body to the content layout
        content_layout.add_widget(body)
        self.add_widget(content_layout)

    def convert(self, instance):
        decimal_input = self.input_text.text
        try:
            hexadecimal_output = self.decimal_to_hexadecimal(decimal_input)
            self.output_text.text = hexadecimal_output
        except ValueError:
            self.output_text.text = 'Invalid Input'

    def decimal_to_hexadecimal(self, num):
        try:
            decimal_num = int(num)
            hexadecimal = hex(decimal_num).replace("0x", "").upper()
            return hexadecimal
        except ValueError:
            raise ValueError('Invalid Input. Please check the input and try again')
    
    def clear(self, instance):
        self.input_text.text = ""
        self.output_text.text = ""
    

    def back(self, instance):
        self.manager.current = "home"

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        
class OctalToHexadecimalScreen(Screen):
    def __init__(self, **kwargs):
        super(OctalToHexadecimalScreen, self).__init__(**kwargs)
        
        # Create a BoxLayout to center the content below the header
        content_layout = MDBoxLayout(orientation="vertical", padding=0, spacing=0)

        # Create a header with a green background color
        header = MDBoxLayout(orientation='horizontal', size_hint=(1, None), height="48dp")
        with header.canvas:
            Color(0.0, 0.5, 0.5, 0.7)  # Teal color (RGBA)
            self.rect = Rectangle(pos=header.pos, size=header.size)

        # Update the background when the position or size changes
        header.bind(pos=self.update_rect, size=self.update_rect)

        # Create a back button
        self.back_button = MDIconButton(icon="arrow-left", on_release=self.back, theme_text_color="Secondary")

        # Create a title label
        self.title_label = MDLabel(text="Octal To Hexadecimal Conversion", halign="center", valign="middle", theme_text_color="Secondary")

        # Add widgets to the header
        header.add_widget(self.back_button)
        header.add_widget(self.title_label)

        # Add the header to the content layout
        content_layout.add_widget(header)
        
        body = MDBoxLayout(orientation="vertical", padding=60, spacing=20)

        

        self.input_text = MDTextField(hint_text="Enter an Octal number")
        self.convert_button = MDFillRoundFlatButton(text="Convert")
        self.convert_button.bind(on_release=self.convert)
        self.clear_button = MDRoundFlatButton(
            text="Clear", on_release=self.clear)
        self.output_label = MDLabel(text="Hexadecimal equivalent:", halign="center")
        self.output_text = MDTextField(readonly=True)

        body.add_widget(self.input_text)
        body.add_widget(self.convert_button)
        body.add_widget(self.clear_button)
        body.add_widget(self.output_label)
        body.add_widget(self.output_text)

        # Add the body to the content layout
        content_layout.add_widget(body)
        self.add_widget(content_layout)

    def convert(self, instance):
        octal_input = self.input_text.text
        try:
            decimal_value = int(octal_input, 8)  # Convert octal to decimal
            hexadecimal_output = self.decimal_to_hexadecimal(decimal_value)
            self.output_text.text = hexadecimal_output
        except ValueError:
            self.output_text.text = 'Invalid Input'

    def decimal_to_hexadecimal(self, num):
        try:
            hexadecimal = hex(num).replace("0x", "").upper()  # Convert decimal to hexadecimal
            return hexadecimal
        except ValueError:
            raise ValueError('Invalid Input. Please check the input and try again')
    
    def clear(self, instance):
        self.input_text.text = ""
        self.output_text.text = ""
    

    def back(self, instance):
        self.manager.current = "home"

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        
class HexadecimalToDecimalScreen(Screen):
    def __init__(self, **kwargs):
        super(HexadecimalToDecimalScreen, self).__init__(**kwargs)
        
        # Create a BoxLayout to center the content below the header
        content_layout = MDBoxLayout(orientation="vertical", padding=0, spacing=0)

        # Create a header with a green background color
        header = MDBoxLayout(orientation='horizontal', size_hint=(1, None), height="48dp")
        with header.canvas:
            Color(0.0, 0.5, 0.5, 0.7)  # Teal color (RGBA)
            self.rect = Rectangle(pos=header.pos, size=header.size)

        # Update the background when the position or size changes
        header.bind(pos=self.update_rect, size=self.update_rect)

        # Create a back button
        self.back_button = MDIconButton(icon="arrow-left", on_release=self.back, theme_text_color="Secondary")

        # Create a title label
        self.title_label = MDLabel(text="Hexadecimal To Decimal Conversion", halign="center", valign="middle", theme_text_color="Secondary")

        # Add widgets to the header
        header.add_widget(self.back_button)
        header.add_widget(self.title_label)

        # Add the header to the content layout
        content_layout.add_widget(header)
        
        body = MDBoxLayout(orientation="vertical", padding=60, spacing=20)

        

        self.input_text = MDTextField(hint_text="Enter a Hexadecimal number")
        self.convert_button = MDFillRoundFlatButton(text="Convert")
        self.convert_button.bind(on_release=self.convert)
        self.clear_button = MDRoundFlatButton(
            text="Clear", on_release=self.clear)
        self.output_label = MDLabel(text="Decimal equivalent:", halign="center")
        self.output_text = MDTextField(readonly=True)

        body.add_widget(self.input_text)
        body.add_widget(self.convert_button)
        body.add_widget(self.clear_button)
        body.add_widget(self.output_label)
        body.add_widget(self.output_text)

        # Add the body to the content layout
        content_layout.add_widget(body)
        self.add_widget(content_layout)

    def convert(self, instance):
        hexadecimal_input = self.input_text.text
        try:
            decimal_output = self.hexadecimal_to_decimal(hexadecimal_input)
            self.output_text.text = decimal_output
        except ValueError:
            self.output_text.text = 'Invalid Input'

    def hexadecimal_to_decimal(self, num):
        try:
            decimal_num = int(num, 16)
            return str(decimal_num)
        except ValueError:
            raise ValueError('Invalid Input. Please check the input and try again')
    
    def clear(self, instance):
        self.input_text.text = ""
        self.output_text.text = ""
    

    def back(self, instance):
        self.manager.current = "home"

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
       
        self.theme_cls = ThemeManager()
        
        # Create a BoxLayout to center the content below the header
        content_layout = MDBoxLayout(orientation="vertical", padding=0, spacing=0)

        # Create a header with a green background color
        header = MDBoxLayout(orientation='horizontal', size_hint=(1, None), height="48dp")
        with header.canvas:
            Color(0.0, 0.5, 0.5, 0.7)  # Teal color (RGBA)
            self.rect = Rectangle(pos=header.pos, size=header.size)

        # Update the background when the position or size changes
        header.bind(pos=self.update_rect, size=self.update_rect)

        # Create a back button
        self.back_button = MDIconButton(icon="arrow-left", on_release=self.back, theme_text_color="Secondary")

        # Create a title label
        self.title_label = MDLabel(text="Settings & Info About App", halign="center", valign="middle", theme_text_color="Secondary")

        self.theme_switch_button = MDIconButton(icon="", theme_text_color="Secondary")

        # Add widgets to the header
        header.add_widget(self.back_button)
        header.add_widget(self.title_label)
        header.add_widget(self.theme_switch_button)

        # Add the header to the content layout
        content_layout.add_widget(header)
        
        self.orientation = "vertical"
        self.padding = "16dp"

        # Create a layout for copyright, powered by, and version information
        body = MDBoxLayout(orientation="vertical", spacing="10dp")
        
        copyright_label = MDLabel(
            text="Designed and Developed by Isaac Gathua - 0745805901",
            theme_text_color="Secondary",
            halign="center"
        )

        powered_label = MDLabel(
            text="Powered by DevsyTech",
            theme_text_color="Secondary",
            halign="center",
            padding=30,
        )

        
        version_label = MDLabel(
            text="Version 0.1.0",
            theme_text_color="Secondary",
            halign="center"
        )

        body.add_widget(copyright_label)
        body.add_widget(powered_label)
        body.add_widget(version_label)

        # Add your settings widgets he
        content_layout.add_widget(body)
        
        self.add_widget(content_layout)  # Add the info layout

       

    def back(self, instance):
        self.manager.current = "home"

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
# Main program entry point
if __name__ == '__main__':
    # Run the Number System Converter App
    NumberSystemConverterApp().run()
