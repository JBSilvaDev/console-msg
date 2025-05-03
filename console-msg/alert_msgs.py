def emsg(msg, bg_color = ''):
  bg = 'm'
  if bg_color == 'black':
    bg = ';40m'
  elif bg_color == 'red':
    bg = ';41m'
  elif bg_color == 'green':
    bg = ';42m'
  elif bg_color == 'yellow':
    bg = ';43m'
  elif bg_color == 'blue':
    bg = ';44m'
  elif bg_color == 'magenta':
    bg = ';45m'
  elif bg_color == 'cyan':
    bg = ';46m'
  elif bg_color == 'white':
    bg = ';47m'
  print(f"\033[31{bg} {msg}\033[00m")

def smsg(msg, bg_color = ''):
  bg = 'm'
  if bg_color == 'black':
    bg = ';40m'
  elif bg_color == 'red':
    bg = ';41m'
  elif bg_color == 'green':
    bg = ';42m'
  elif bg_color == 'yellow':
    bg = ';43m'
  elif bg_color == 'blue':
    bg = ';44m'
  elif bg_color == 'magenta':
    bg = ';45m'
  elif bg_color == 'cyan':
    bg = ';46m'
  elif bg_color == 'white':
    bg = ';47m'
  print(f"\033[32{bg} {msg}\033[00m")
  
def almsg(msg, bg_color = ''):
  bg = 'm'
  if bg_color == 'black':
    bg = ';40m'
  elif bg_color == 'red':
    bg = ';41m'
  elif bg_color == 'green':
    bg = ';42m'
  elif bg_color == 'yellow':
    bg = ';43m'
  elif bg_color == 'blue':
    bg = ';44m'
  elif bg_color == 'magenta':
    bg = ';45m'
  elif bg_color == 'cyan':
    bg = ';46m'
  elif bg_color == 'white':
    bg = ';47m'
  print(f"\033[33{bg} {msg}\033[00m")

def imsg(msg, bg_color = ''):
  bg = 'm'
  if bg_color == 'black':
    bg = ';40m'
  elif bg_color == 'red':
    bg = ';41m'
  elif bg_color == 'green':
    bg = ';42m'
  elif bg_color == 'yellow':
    bg = ';43m'
  elif bg_color == 'blue':
    bg = ';44m'
  elif bg_color == 'magenta':
    bg = ';45m'
  elif bg_color == 'cyan':
    bg = ';46m'
  elif bg_color == 'white':
    bg = ';47m'
  print(f"\033[34{bg} {msg}\033[00m")


# O pacote console-msg é utilizado para:
# 	- Exibir mensagens personalizadas no terminal
#     - Mensagem de erro (vermelho)
#     - Mensagem de sucesso (verde)
#     - Mensagem de alerta (amarelo)
#     - Mensagem de informação (azul)