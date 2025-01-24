import socket
import threading
import readline

SERVER = "127.0.0.1"
PORT = 1234

def unpack_message(data):
    try:
        name_size = data[0]
        message_size = data[1]

        if len(data) < 2 + name_size + message_size:
            raise ValueError("Dados insuficientes para o nome e mensagem.")

        userName = data[2:2 + name_size].decode('utf-8')
        message = data[2 + name_size:2 + name_size + message_size].decode('utf-8')

        return userName, message
    except Exception as e:
        print(f"Erro ao desempacotar dados: {e}")
        raise

def listen(client):
    while True:
        try:
            otherUserMsg, address = client.recvfrom(1024)
            if otherUserMsg:
                userName, message = unpack_message(otherUserMsg)
                print(f"{userName} disse: {message}")
        except Exception as e:
            print(f"Erro ao ouvir mensagens do servidor: {e}")
            break


def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        userName = input("Qual seu nome de usuário? ").strip()[:255]
        userName_bytes = userName.encode('utf-8')
        client.sendto("".encode('utf-8'), (SERVER, PORT))

        threading.Thread(target=listen, args=(client, ), daemon=True).start()

        while True:
            message = input("").strip()[:255]

            if message != "":
                readline.get_line_buffer()
                print("\033[A\033[K", end="") # Removendo o input do texto digitado

                message_bytes = message.encode('utf-8')

                packed_data = bytes([len(userName_bytes), len(message_bytes)]) + userName_bytes + message_bytes
                client.sendto(packed_data, (SERVER, PORT))
                print(f"Você disse: {message}")
            else:
                print("Erro: a mensagem deve conter conteúdo para ser enviada.")
    except Exception as e:
        print(f"Erro no cliente: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()
