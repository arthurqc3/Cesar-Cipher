from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
direction = input("Digite 'codificar' para encriptar, digite 'decodificar' para desencriptar:\n")
text = input("Digite sua mensagem:\n").lower()
shift = int(input("Digite o numero para trocar de posição:\n"))

def ceasar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decodificar":
    shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    end_text += new_letter
  print(f"O texto resultante é {end_text}")

ceasar(start_text = text, shift_amount = shift, cipher_direction = direction)