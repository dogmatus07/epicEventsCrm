from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich import box
from datetime import datetime

console = Console()


def display_client_list(clients):
    """
    Display a list of clients
    :param clients:
    :return: list of clients
    """
    table = Table(title="[bold blue]✨Liste des clients✨[/]", box=box.ROUNDED)
    table.add_column("[bold green]ID[/]", style="dim", width=12)
    table.add_column("[bold green]Nom complet[/]")
    table.add_column("[bold green]E-mail[/]")
    table.add_column("[bold green]Téléphone[/]")
    table.add_column("[bold green]Société[/]", style="blue")
    table.add_column("[bold green]Date premier contact[/]")
    table.add_column("[bold green]Date mise à jour[/]")
    table.add_column("[bold green]Commercial[/]")
    for client in clients:
        commercial_name = client.commercial.full_name if client.commercial else "Non attribué"
        table.add_row(
            str(client.id),
            client.full_name,
            client.email,
            client.phone,
            client.company_name,
            client.first_contact_date,
            client.last_update_date,
            commercial_name
        )
    console.print(Panel(table, title="🚀 Clients", expand=False))


def create_client():
    """
    Display a form for creating a new client
    :return: dictionary with client data
    """
    console.print("[bold blue]➕ Création d'un nouveau client ➕[/]\n")
    full_name = Prompt.ask("[bold cyan]Nom complet du client[/]", default="John Doe")
    email = Prompt.ask("[bold cyan]E-mail du client[/]", default="adresse@email.com")
    phone = Prompt.ask("[bold cyan]Téléphone du client[/]", default="0102030405")
    company_name = Prompt.ask("[bold cyan]Nom de la société du client[/]", default="Ma Société")
    first_contact_date_str = Prompt.ask("[bold cyan]Date du premier contact (DD-MM-YYYY)[/]", default=datetime.now().date())
    last_update_date_str = Prompt.ask("[bold cyan]Date  mise à jour (DD-MM-YYYY)[/]", default=datetime.now().date())

    try:
        first_contact_date = datetime.strptime(first_contact_date_str, "%d-%m-%Y").date()
        last_update_date = datetime.strptime(last_update_date_str, "%d-%m-%Y").date()
    except ValueError:
        console.print("[bold red]❌ Les dates doivent être au format DD-MM-YYYY[/]")
        return None

    return {
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "company_name": company_name,
        "first_contact_date": first_contact_date,
        "last_update_date": last_update_date
    }


def update_client(client):
    """
    display a form for updating a client
    :param client:
    :return: updated client data
    """
    console.print("[bold blue]🔄 Modification du client : {client.full_name}🔄[/]\n")

    full_name = Prompt.ask("[bold cyan]Nom complet du client[/]", default=client.full_name)
    email = Prompt.ask("[bold cyan]E-mail du client[/]", default=client.email)
    phone = Prompt.ask("[bold cyan]Téléphone du client[/]", default=client.phone)
    company_name = Prompt.ask("[bold cyan]Nom de la société du client[/]", default=client.company_name)
    first_contact_date_str = Prompt.ask(
        "[bold cyan]Date du premier contact (DD-MM-YYYY)[/]",
        default=client.first_contact_date.strftime("%d-%m-%Y")
    )
    last_update_date_str = Prompt.ask(
        "[bold cyan]Date  mise à jour (DD-MM-YYYY)[/]",
        default=client.last_update_date.strftime("%d-%m-%Y")
    )

    try:
        first_contact_date = datetime.strptime(first_contact_date_str, "%d-%m-%Y").date()
        last_update_date = datetime.strptime(last_update_date_str, "%d-%m-%Y").date()
    except ValueError:
        console.print("[bold red]❌ Les dates doivent être au format DD-MM-YYYY[/]")
        return None

    return {
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "company_name": company_name,
        "first_contact_date": first_contact_date,
        "last_update_date": last_update_date
    }


def delete_client(client):
    """
    Ask confirmation before deleting a client
    :param client: 
    :return: confirmation
    """
    console.print(f"[bold red]⚠️ Suppression du client {client.full_name}[/]")
    return Confirm.ask("Confirmez-vous la suppression du client ?")
