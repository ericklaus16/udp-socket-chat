## UDP Chat Server

Um sistema simples de chat utilizando sockets UDP em Python. Este projeto implementa um servidor e um cliente que permitem comunicação em tempo real entre múltiplos usuários na mesma rede.

### 📋 Funcionalidades

* Conexão de clientes: Os usuários são adicionados automaticamente à lista de clientes ativos ao enviar um pacote vazio ("").
* Mensagens em tempo real: Os clientes podem trocar mensagens instantaneamente com todos os participantes conectados.
* Gerenciamento de clientes: O servidor identifica e armazena os endereços dos clientes que estão ativos.
* Mensagens privadas e difusão: O servidor transmite mensagens recebidas para todos os outros clientes conectados.

### 🛠️ Tecnologias Utilizadas

* Python 3: Linguagem de programação base para o desenvolvimento.
* Sockets UDP: Protocolo para comunicação de rede entre servidor e clientes.

### 🚀 Como Executar

Clone este repositório:

```bash
git clone https://github.com/seu-usuario/udp-chat-server.git
cd udp-chat-server
```

Inicie o servidor:

```bash
python server.py
```

Em outro terminal, execute o cliente:

```bash
python client.py
```

Digite o nome do cliente e uma mensagem no cliente e veja a comunicação funcionando em tempo real.

### 📦 Estrutura do Projeto

```bash
udp-chat-server/
├── server.py  # Código do servidor UDP
├── client.py  # Código do cliente UDP
└── README.md  # Documentação do repositório
```