import os
import pyfiglet

options = {
    '1': 'Generate ASCII Art',
    'c': 'Change Console Color',
    'q': 'Quit'
}

ascii_text = pyfiglet.figlet_format('ASCII ART GENERATOR')
goodbye_text = pyfiglet.figlet_format('Goodbye!')

console_colors = {
    'black': '0',
    'blue': '1',
    'green': '2',
    'aqua': '3',
    'red': '4',
    'purple': '5',
    'yellow': '6',
    'white': '7',
    'gray': '8',
    'light blue': '9',
}

def change_console_color():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format('Color Selector'))
    print('Console Color Options:\n')
    for key, value in console_colors.items():
        print(f'{key.capitalize()}: {value}')
    while True:
        color_choice = input('Enter the color code you want to set: ').lower()
        if color_choice in console_colors.values():
            os.system(f'color {color_choice}')
            confirm = input(f'Are you sure you want to set console color to {color_choice}? (y/n)').lower()
            if confirm == 'y':
                os.system('cls' if os.name == 'nt' else 'clear')
                print(pyfiglet.figlet_format('ASCII ART GENERATOR'))
                break
            elif confirm == 'n':
                continue
            else:
                print('Invalid choice. Please try again.')
        else:
            print('Invalid choice. Please try again.')
    

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
        elif choice == 'c':
            change_console_color()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(goodbye_text)
            break
    else:
        print('Invalid choice. Please try again.')
