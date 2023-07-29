# Kivy-Node-RED-Integration

# Descrição
Este repositório contém um projeto de integração entre o framework Kivy e o Node-RED. O Kivy é uma biblioteca Python para criar interfaces gráficas multiplataforma e interativas, enquanto o Node-RED é uma ferramenta de programação visual para conectar dispositivos, APIs e serviços na Internet das Coisas (IoT).

# Objetivo
O objetivo deste projeto é demonstrar como é possível usar o Kivy para criar uma interface gráfica para interagir com o Node-RED, permitindo a troca de dados entre o aplicativo Kivy e os fluxos criados no Node-RED. O repositório inclui exemplos de código e uma documentação detalhada para facilitar a integração e a compreensão dos conceitos envolvidos.

# Integração Kivy com Node-RED
Este projeto tem como objetivo demonstrar como integrar o framework Kivy com o Node-RED para criar aplicações interativas e conectadas.

# Como usar o aplicativo Kivy:
1. Clone este repositório em seu ambiente local.
2. Certifique-se de ter o Kivy e a biblioteca requests instalados (pip install kivy requests).
3. Execute o aplicativo Kivy usando o arquivo main.py.
4. Digite a mensagem desejada na interface gráfica e clique no botão "Enviar".
5. O aplicativo enviará a mensagem para o Node-RED usando uma requisição HTTP POST.
6. Confira o console do Node-RED para ver a mensagem recebida e processada.

# Como usar o Node-RED Flow:
1. Certifique-se de ter o Node-RED instalado em sua máquina.
2. Abra o Node-RED em seu navegador (geralmente em http://localhost:1880).
3. Importe os fluxos Node-RED fornecidos neste repositório.
4. Conecte o fluxo de entrada a uma fonte de dados externa ou a um nó de teste.
5. Ao receber uma mensagem, o fluxo enviará uma resposta de volta ao aplicativo Kivy.

Este projeto é apenas uma demonstração de conceito e pode ser estendido e adaptado para atender às necessidades específicas do seu projeto. Sinta-se à vontade para explorar, modificar e contribuir para o repositório!

Importante: Este repositório contém apenas fins educacionais e para demonstrar a integração entre o Kivy e o Node-RED. Certifique-se de não incluir informações sensíveis em suas aplicações e fluxos de produção.
