import socket

ADDR = "127.0.0.1"
PORT = 1234

chatters = []

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

def main():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind((ADDR, PORT))
        print(f"Servidor iniciado em {ADDR}:{PORT}")

        while True:
            try:
                data, address = server.recvfrom(1024)
                if not data:
                    if address not in chatters:
                        chatters.append(address)
                        print(f"Novo cliente adicionado: {address}. Total: {len(chatters)} clientes.")
                        continue
            
                print(f"Recebido de {address}: {len(data)} bytes")

                userName, message = unpack_message(data)
                retorno = f"{userName} disse: {message}".encode('utf-8')

                for chatter in chatters:
                    if chatter != address:
                        server.sendto(data, chatter)

            except ValueError as ve:
                print(f"Erro ao desempacotar dados: {ve}")
            except Exception as e:
                print(f"Erro inesperado: {e}")

    except KeyboardInterrupt:
        print("\nServidor encerrado pelo usuário.")
    except Exception as e:
        print(f"Erro fatal no servidor: {e}")
    finally:
        server.close()

if __name__ == "__main__":
    main()
