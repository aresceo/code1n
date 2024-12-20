import time
import telebot

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

# Applica la sfumatura di verde.
print(green_gradient(ascii_art))


# La scritta ASCII del canale Telegram
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

# Funzione per cercare il tag nel canale Telegram
def check_tag_in_channel(bot, chat_id, tag):
    try:
        # Recupera i messaggi dal canale
        for message in bot.get_chat_administrators(chat_id):
            if tag in message.text:
                return True  # Se il tag è presente in uno dei messaggi
        return False  # Se il tag non è trovato
    except Exception as e:
        print(f"Errore durante la ricerca del tag nel canale: {e}")
        return False

# Funzione per gestire la scelta dell'utente
def main():
    print(ascii_art)  # Stampa la scritta ASCII iniziale

    # Pausa per un effetto di attesa
    time.sleep(1)

    # Stampa le opzioni
    print("1. Prova")
    print("2. Test")

    # Prendi l'input dell'utente
    scelta = input("Scegli un'opzione (1 o 2): ")

    if scelta == "1":
        # Se l'utente sceglie "1", stampa il messaggio del canale
        print(ascii_channel)
        print("Il mio canale Telegram @executedban")

if __name__ == "__main__":
    main()
