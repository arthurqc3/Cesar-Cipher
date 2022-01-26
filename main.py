from art import logo
from alphabet import alphabet

print(logo)

def ceasar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decodificar":
   shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"O texto resultante é {end_text}")

again = True

while again:
  direction = input("Digite 'codificar' para encriptar, digite 'decodificar' para desencriptar:\n")
  text = input("Digite sua mensagem:\n").lower()
  shift = int(input("Digite o numero para trocar de posição:\n"))
  shift = shift % 26   

  ceasar(start_text = text, shift_amount = shift, cipher_direction = direction)

  result = input("Você desejar usar novamente? digite SIM ou NAO\n").lower()
  if result == "nao":
    print("Até mais o/")
    again = False