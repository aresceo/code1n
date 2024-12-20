import time

# La scritta ASCII che incollerai
ascii_art = """                                                    
 ▓█████▒██   ██▒ ▓█████  ▄████▄  █    ██ ▄▄▄█████▓ ▓█████▓█████▄  ▄▄▄▄    ▄▄▄      ███▄    █ 
 ▓█   ▀▒▒ █ █ ▒░ ▓█   ▀ ▒██▀ ▀█  ██  ▓██▒▓  ██▒ ▓▒ ▓█   ▀▒██▀ ██▌▓█████▄ ▒████▄    ██ ▀█   █ 
 ▒███  ░░  █   ░ ▒███   ▒▓█    ▄▓██  ▒██░▒ ▓██░ ▒░ ▒███  ░██   █▌▒██▒ ▄██▒██  ▀█▄ ▓██  ▀█ ██▒
 ▒▓█  ▄ ░ █ █ ▒  ▒▓█  ▄▒▒▓▓▄ ▄██▓▓█  ░██░░ ▓██▓ ░  ▒▓█  ▄░▓█▄   ▌▒██░█▀  ░██▄▄▄▄██▓██▒  ▐▌██▒
▒░▒████▒██▒ ▒██▒▒░▒████░▒ ▓███▀ ▒▒█████▓   ▒██▒ ░ ▒░▒████░▒████▓ ░▓█  ▀█▓▒▓█   ▓██▒██░   ▓██░
░░░ ▒░ ▒▒ ░ ░▓ ░░░░ ▒░ ░░ ░▒ ▒  ░▒▓▒ ▒ ▒   ▒ ░░   ░░░ ▒░  ▒▒▓  ▒ ░▒▓███▀▒░▒▒   ▓▒█░ ▒░   ▒ ▒ 
░ ░ ░  ░░   ░▒ ░░ ░ ░     ░  ▒  ░░▒░ ░ ░     ░    ░ ░ ░   ░ ▒  ▒ ▒░▒   ░ ░ ░   ▒▒ ░ ░░   ░ ▒░
    ░   ░    ░      ░   ░        ░░░ ░ ░   ░          ░   ░ ░  ░  ░    ░   ░   ▒     ░   ░ ░ 
░   ░   ░    ░  ░   ░   ░ ░        ░              ░   ░     ░     ░            ░           ░                                            
"""

ascii_channel = """     
  ▄▄▄▄▄        ▄▄▄▄      ▄▄▄▄▄▄▄▄ ███████ ████████   ▄█▄  ▄█▄   
  ███  ██      ████    ▀██▄▄▄█████████████ ██▄▄█████   ██   ███  
  ██    ██    ▄██▄  ▄███████████████▀████████████████████  █████ 
 ██     ██   ▄██▀ ██   ▀███▀ ███████████  ██████████  ▄████████
 ████████   ▄██▀  ██▄▄█▀    ██▀   ██████  ▄██████████▄ ███████
██        ██    ██ ███████▄   ██████ █████ ██████████ ▄██▀   
 ███▄   ███▄    ██ ██ ███▄ ▄█▀    ▀████  ███▄▄██████████      
      ▀▀███▀   ▀▀▀  ██████████▄▄▄▄██▀  ▀███████████████▄ █     
"""

# Funzione per creare una sfumatura di verde.
def green_gradient(ascii_art):
    lines = ascii_art.split("\n")
    num_lines = len(lines)
    gradient_text = ""

    for i, line in enumerate(lines):
        # Calcoliamo il valore di verde basato sulla posizione della riga.
        green_value = int(255 * (i / max(1, num_lines - 1)))
        color_code = f"\033[38;2;0;{green_value};0m"  # Verde sfumato.
        gradient_text += f"{color_code}{line}\033[0m\n"  # Reset colore alla fine di ogni riga.

    return gradient_text

# Funzione principale
def main():
    # Stampa la scritta con la sfumatura di verde
    print(green_gradient(ascii_art))  

    # Pausa per un effetto di attesa
    time.sleep(1)

    # Stampa le opzioni
    print("1. Mostra il messaggio del canale")
    print("2. Esci")

    # Prendi l'input dell'utente
    scelta = input("Scegli un'opzione (1 o 2): ")

    if scelta == "1":
        # Stampa la scritta del canale con sfumatura
        print(green_gradient(ascii_channel))
        print("Il mio canale Telegram: @executedban")
    elif scelta == "2":
        print("Uscita dal programma.")
    else:
        print("Scelta non valida. Riprova.")

# Avvio del programma
if __name__ == "__main__":
    main()
