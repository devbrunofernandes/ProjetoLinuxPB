# Configuração do Servidor Web

A segunda etapa consiste na instalação e na configuração do software **Nginx** que será utilizado para servir requisições de página web. 

## Entrando como usuário root

Caso não esteja iniciada, inicie a máquina virtual e abra o seu terminal, com o terminal aberto digite o comando "**sudo su**" para entrar como usuário _root_, será pedido a senha de acesso do seu usuário para autentificação, essa senha foi definida durante a instalação do sistema operacional, insira a senha e você estará logado como usuário root.

## Instalação do Nginx

O processo de instalação é bem simples, digite o comando "**apt update**" para atualizar a base de pacotes disponíveis para serem instalados com o gerenciador de pacotes **apt**, e então digite comando "**apt-get install nginx**", aparecerá uma mensagem na tela pedindo confirmação da instalação, aceite e aguarde o término do processo.

![Terminal instalando nginx](Imagens/Imagem5.PNG)

Você pode utilizar um comando "**service nginx status**" para verificar se o serviço está instalado corretamente e está ativo.

## Criando arquivo HTML

Navegue para o diretório "**/var/www/html**" usando o comando "**cd /var/www/html**", com o comando "**ls**" é possível ver que só existe o arquivo "**index.nginx-debian.html**", para criar o arquivo .html da nossa página, use o comando "**nano index.html**" que abrirá o editor de texto para criação do "**index.html**", a configuração padrão do nginx faz que automaticamente ele será detectado como página padrão do servidor.

Com o editor de texto aberto, você pode escrever o conteúdo da sua página HTML livremente, ao terminar de editar, salve (com CTRL + O se estiver utilizando o **nano**) e feche o arquivo (com CTRL + X no mesmo caso).

Clique para visualizar o conteúdo do meu arquivo [index.html](index.html).

![Página HTML](Imagens/Imagem6.PNG)

## Automatizando reinicio do Nginx

Para isso, vamos criar um serviço systemd para o Nginx, fazendo com que ele reinicie automaticamente sempre em caso de falha.

Utilize o comando "**systemctl edit nginx.service**", esse comando criará um arquivo que adiciona configurações aos padrões do Nginx sem modificar os arquivos originais, ele também abrirá o editor de texto para modificar o arquivo que estará cheio de comentários, pode escrever as configurações logo após o primeiro bloco de comentários.

O que deve ser escrito é, "**[Service]**" para indicar que se trata de configurações de serviço do processo, logo abaixo "**Restart=on-failure**" que indica para reiniciar o serviço em caso de falha, e mais uma linha embaixo "**RestartSec=5s**" para dar tempo ao sistema reiniciar o processo sem gerar muitos pedidos para essa tarefa.

Salve as alterações e feche o arquivo, agora para verificar se deu certo utilize o comando "**systemctl status nginx.service**" e procure pela linha "**Drop-In**" contendo "**override.conf**".

Isso finaliza a etapa 2 **Configuração do Servidor Web** para seguir clique em [próximo](MONITORAMENTO.md).