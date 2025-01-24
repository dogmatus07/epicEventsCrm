from rich.prompt import Prompt
from rich.console import Console

from crm.controllers import (
    client_controller,
    contract_controller,
    event_controller,
    user_controller,
    auth_controller
)
from crm.views import (
    client_views,
    contract_views,
    event_views,
    user_views
)
from db.session import get_db

console = Console()


def main_menu(user):
    """
    Display the main menu
    """
    db = next(get_db())

    while True: