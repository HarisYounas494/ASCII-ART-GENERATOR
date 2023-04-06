import os
import pyfiglet

options = {
    '1': 'Start !',
    'q': 'Quit'
}

ascii_text = '''
 /$$$$$$$$  /$$$$$$$$  /$$   /$$  /$$$$$$$$  /$$$$$$  /$$$$$$$    /$$$$$$    /$$$$$$ 
|_____ $$  | $$_____/ | $$$ | $$ |__  $$__/ |_  $$_/ | $$__  $$  /$$__  $$  /$$__  $$
     /$$/  | $$       | $$$$| $$    | $$      | $$   | $$  \ $$ | $$  \ $$ | $$  \__/
    /$$/   | $$$$$    | $$ $$ $$    | $$      | $$   | $$$$$$$/ | $$  | $$ | $$ /$$$$
   /$$/    | $$__/    | $$  $$$$    | $$      | $$   | $$__  $$ | $$  | $$ | $$|_  $$
  /$$/     | $$       | $$\  $$$    | $$      | $$   | $$  \ $$ | $$  | $$ | $$  \ $$
 /$$$$$$$$ | $$$$$$$$ | $$ \  $$    | $$     /$$$$$$ | $$  | $$ |  $$$$$$/ |  $$$$$$/
|________/ |________/ |__/  \__/    |__/    |______/ |__/  |__/  \______/   \______/ 

                                                         ( Made By Haris Younas )
'''

print(ascii_text)

while True:
    print('-' * 20)
    for key, value in options.items():
        print(f'{key}: {value}')
    print('-' * 20)

    choice = input('Enter your choice: ').lower()

    if choice in options:
        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            fonts = pyfiglet.FigletFont.getFonts()
            print("Fonts Available on Your System:\n")
            for font in fonts:
                print(font)
            selected_font = input("\nEnter the font name to be used: ")
            text = input('Enter the text to be converted: ')
            custom_font = pyfiglet.Figlet(font=selected_font)
            ascii_art = custom_font.renderText(text)
            print(ascii_art)
            while True:
                generate_again = input('Generate again? (y/n): ').lower()
                if generate_again == 'y':
                    text = input('Enter the text to be converted: ')
                    ascii_art = custom_font.renderText(text)
                    print(ascii_art)
                elif generate_again == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(ascii_text)
                    break
                else:
                    print('Invalid choice. Please try again.')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(pyfiglet.figlet_format('Goodbye!'))
            break
    else:
        print('Invalid choice. Please try again.')
