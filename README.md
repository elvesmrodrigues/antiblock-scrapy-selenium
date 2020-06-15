# antiblock_scrapy_selenium

Este módulo é uma extensão para o projeto de [scrapy-selenium](https://github.com/clemfromspace/scrapy-selenium). 

O principal uso do **scrapy-selenium** é para o caso de sites que precisam processar javascript para renderizar seu conteúdo. Por outro lado, mecanismos antibloqueios básicos de coletas não se encontram no projeto original.

Scrapy-selenium foi extendido usando como base [antiblock-selenium](https://github.com/elvesrodrigues/antiblock-selenium), que permite rotacionar IPs via Tor, definir delays entre requisições (aleatório ou fixo), rotacionar user-agents, além de persistir/carregar cookies.

**Obs.: Não há compatibilidade com selenium remoto neste projeto.** 

## Funcionalidades

Junção de **scrapy-selenium** com **antiblock-selenium**, ou seja:

- Permitir carregar sites que necessitam javascript ao Scrapy, entre outras funcionalidades do **scrapy-selenium**
- Evitar bloqueios em coletas, por meio de:
    - Rotação de IPs via Tor
    - Rotação de user-agents
    - Delays aleatórios ou fixos entre requisições
    - Persistir/carregar cookies

## Instalação

Maneira mais fácil:

```bash
pip install antiblock-scrapy-selenium
```
## Configuração

Siga os passos de configuração do Tor em [antiblock-selenium](https://github.com/elvesrodrigues/antiblock-selenium).

Os navegadores suportados são:
- Chrome
- Firefox


## Uso

**Básico**:

- Ativação do Middleware: 
    ```bash
    DOWNLOADER_MIDDLEWARES = {
        'antiblock_scrapy_selenium.SeleniumMiddleware': 800
    }
    ```
- Adicione o navegador a ser usado, o local da executável do driver do navegador e os argumentos a serem passados para o driver:
    ```python
    #settings.py
    from shutil import which

    SELENIUM_DRIVER_NAME = 'firefox' #ou chrome
    SELENIUM_DRIVER_EXECUTABLE_PATH = which('geckodriver')
    SELENIUM_DRIVER_ARGUMENTS=['-headless']  # '--headless' se estiver usando chrome
    ```
- Opcionalmente, defina o local da executável do navegador:
    ```python
    SELENIUM_BROWSER_EXECUTABLE_PATH = which('firefox')
    ```
- Use `antiblock_scrapy_selenium.SeleniumRequest` ao invés de `Request` do Scrapy, como abaixo:
    ```python 
    from antiblock_scrapy_selenium import SeleniumRequest

    yield SeleniumRequest(url=url, callback=self.parse_result)
    ```
    - Exemplo com um Spider:
        ```python
        import scrapy

        from antiblock_scrapy_selenium import SeleniumRequest

        class FooSpider(scrapy.Spider):
            name = 'foo'
            
            def start_requests(self):
                url = 'https://alguma-url'

                yield SeleniumRequest(url=url, callback=self.parse)

            def parse(self, response):
                pass
        ```
- Utilize as demais funcionalidades do `scrapy-selenium` normalmente, disponíveis [aqui]().

> **O Parâmetro SELENIUM_COMMAND_EXECUTOR do scrapy-selenium não é suportada.**
