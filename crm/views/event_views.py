from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich import box
from datetime import datetime

from ..controllers import contract_controller, user_controller
from ..views import user_views, contract_views

console = Console()

