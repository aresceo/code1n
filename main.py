import time
import telebot

# La scritta ASCII che incollerai
ascii_art = """                                                    
  ▄▄█▀▀▀█▄█ ▄▄█▀▀██▄ ▀███▀▀▀██▄ ▀███▀▀▀███▀████▀███▄   ▀███▀
▄██▀     ▀███▀    ▀██▄ ██    ▀██▄ ██    ▀█  ██   ███▄    █  
██▀       ▀█▀      ▀██ ██     ▀██ ██   █    ██   █ ███   █  
██        ██        ██ ██      ██ ██████    ██   █  ▀██▄ █  
██▄       ██▄      ▄██ ██     ▄██ ██   █  ▄ ██   █   ▀██▄█  
▀██▄     ▄▀██▄    ▄██▀ ██    ▄██▀ ██     ▄█ ██   █     ███  
  ▀▀█████▀  ▀▀████▀▀ ▄████████▀ ▄██████████████▄███▄    ██                                             
"""

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
