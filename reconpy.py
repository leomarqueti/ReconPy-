import requests
from rich import print
import os
from rich.panel import Panel
from rich.prompt import Prompt

headers = {
"User-Agent": "ReconPy/1.0 (OSINT Tool; contact: youremail@example.com)",
"Accept": "application/json"
}

def banner():
    limpar()
    print("""
[bright_yellow]
 ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██████╗ ██╗   ██╗
 ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║██╔══██╗╚██╗ ██╔╝
 ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║██████╔╝ ╚████╔╝ 
 ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║██╔═══╝   ╚██╔╝  
 ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██║        ██║   
 ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝        ╚═╝   
[/bright_yellow]
[dim]ReconPy v0.1 | Python OSINT Toolkit[/dim]
""")

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    print("\n[bright_yellow]Pressione Enter para voltar ao menu...[/bright_yellow]")
    input()
    limpar()

def buscar_ip(ip):

    try:
        url = f'http://ip-api.com/json/{ip}'

        r = requests.get(url, headers=headers)

        dados_json = r.json()

        if dados_json['status'] == "fail":
            return "[red]Erro: Ip nao encontrado![/red]"
        else:
            return dados_json
    except:
        return "[red]Ocorreu um erro[/red]"
    
def listar_dados_ip(dados):

    try:
        print(Panel(f"IP: [green]{dados["query"]}[/green]\n"
                    f"Pais: [green]{dados["country"]}[/green]\n"
                    f"Cidade: [green]{dados["city"]}[/green]\n"
                    f"Região: [green]{dados["regionName"]}[/green]\n"
                    f"Provedor: [green]{dados["org"]}[/green]", title="ReconPy", style="cyan"))
    except:
        print(dados)

def pegar_ip_alvo():
    limpar()
    print(Panel(
        "[bold cyan]IP Lookup[/bold cyan]\n\n"
        "Informe o IP para consulta",
        title="ReconPy",
        border_style="bright_cyan"
    ))

    ip = input("IP alvo: ")

    dados = buscar_ip(ip)

    listar_dados_ip(dados)

    pausar()

def mostrar_menu():
    print(Panel("[1] IP Lookup\n""[2] Username Recon\n""[3] Sair", title="ReconPy", style="cyan"))
    
def check_github(username):
    r = requests.get(f"https://api.github.com/users/{username}",
        headers=headers)
    
    if r.status_code == 200:
        dados = r.json()
        return dados 
    else:
        return "Username não encontrado"
    
def check_reddit(username):
    r = requests.get(f"https://www.reddit.com/user/{username}/about.json",
        headers=headers)
    
    if r.status_code == 200:
        dados = r.json()
        return dados 
    else:
        return "Username não encontrado"
  
def listar_dados_username(username):

    github = check_github(username)
    reddit = check_reddit(username)

    if github != "Username não encontrado":
        localizacao = github["location"]
        if localizacao:
            local = localizacao
        else: 
            local = "Não encontrado"
        print(Panel(f"User: [green]{github["login"]}[/green]\n"
                    f"Url: [green]{github["url"]}[/green]\n"
                    f"Nome: [green]{github["name"]}[/green]\n"
                    f"Criada em: [green]{github["created_at"]}[/green]\n"
                    f"Localização: [green]{local}[/green]", title="GITHUB", style="cyan"))
    else:
        print(Panel(f"User: [red]{"Username não encontrado!!"}[/red]\n"
                    , title="GITHUB", style="cyan"))
        
    if reddit != "Username não encontrado":
        print(Panel(f"User: [green]{reddit["data"]["name"]}[/green]\n"
                    f"Url: [green]{f"https://www.reddit.com/user/{username}"}[/green]\n"
                    , title="REDDIT", style="cyan"))
    else:
        print(Panel(f"User: [red]{"Username não encontrado!!"}[/red]\n"
                    , title="REDDIT", style="cyan"))

def pegar_username():
    limpar()
    print(Panel(
        "[bold cyan]Username Recon[/bold cyan]\n\n"
        "Informe o USERNAME para consulta",
        title="ReconPy",
        border_style="bright_cyan"
    ))

    username = input("USERNAME alvo: ")

    listar_dados_username(username)

    pausar()

def iniciar():
    
    continuar = True

    while continuar:
        banner()
        mostrar_menu()

        op = Prompt.ask("[bold cyan]Selecione uma opção[/bold cyan]")

        if op == "1":
            pegar_ip_alvo()
        if op == "2":
            pegar_username()
        if op == "3":
            continuar = False

iniciar()
    

