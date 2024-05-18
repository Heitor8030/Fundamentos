import time

def countdown_timer():
    """
    Função que exibe um contador regressivo com base na entrada do usuário.
    """
    minutes = int(input("Digite o número de minutos: "))
    seconds = int(input("Digite o número de segundos: "))
    
    total_seconds = minutes * 60 + seconds
    
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    
    print('O tempo acabou!')

# Chamar a função
countdown_timer()