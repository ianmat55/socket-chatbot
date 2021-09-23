from rich.theme import Theme
from rich.console import Console
from rich.table import Table
from rich.layout import Layout
from rich.panel import Panel
import shutil

############################# Color Schemes ####################################
cyberpunk = {"title": "#c8b029", 
	     "title2": "#e68e35",
	     "error": "#dd517e",
	     "reg": "#145e98",
	     "user": "#0abdc6",
	     "user2": "red",
	     "server": "#ab5797",
	     }

obsidian = {
	"title": "#483699",
	"user": "#78781b",
	"text": "white",
	"banana": "#f1d46d",
	"peach": "#f1d46d",
	"strawberry": "#e280e9",
	"dark_purp": "#9370f6",
	"midnight": "#5365ff",
	"wine": "#de4383",
	"orange": "#f8a978"
}
############################# ASCII ART and UX #################################
theme = Theme(obsidian)
console = Console(theme=theme)

cols, rows = shutil.get_terminal_size() # get size of terminal for automatic centering

chatty = """
=====================================================
=                                                   =
=                                                   =
=                ╭━━━┳╮╱╱╱╱╭╮╱╭╮                    =
=                ┃╭━╮┃┃╱╱╱╭╯╰┳╯╰╮                   =
=                ┃┃╱╰┫╰━┳━┻╮╭┻╮╭╋╮╱╭╮               =
=                ┃┃╱╭┫╭╮┃╭╮┃┃╱┃┃┃┃╱┃┃               =
=                ┃╰━╯┃┃┃┃╭╮┃╰╮┃╰┫╰━╯┃               =
=                ╰━━━┻╯╰┻╯╰┻━╯╰━┻━╮╭╯               =
=                ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃                =
=                ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯                =
=                                                   =
=                                                   =
=====================================================
"""

# center multi-line ascii art
l1 = chatty.split("\n")
def padToCenter(text, width):
	return '\n'.join(x.center(width) for x in text)

title = padToCenter(l1, cols)

# Server command table created with rich library
def print_server_help():
	table_s = Table(title="Server Commands", style="dark_purp")

	# table columns
	table_s.add_column("Command", style="orange")
	table_s.add_column("Description", style="orange")

	# table rows
	table_s.add_row("BC()", "Broadcast a message to a specific client")
	table_s.add_row("CLS()", "Clear the screen")
	table_s.add_row("HELP()", "Provide information for server commands")
	table_s.add_row("KICK()", "Kick a client from the server")
	table_s.add_row("LS()", "List current connections")
	table_s.add_row("READ()", "Read and send contents of text file")
	table_s.add_row("'ctrl+c' to exit")

	console.print(table_s, style="peach", justify="center")
	print('[*] Just a fun project to learn about socket communication')


def print_client_help():
	# Client command table created with rich library
	table_c = Table(title="Client Commands", style="dark_purp")

	# table columns
	table_c.add_column("Command", style="orange")
	table_c.add_column("Description", style="orange")

	# table rows
	table_c.add_row("EXIT()", "Disconnect from server")
	table_c.add_row("READ()", "Read and send contents of text file")
	table_c.add_row("CLS()", "Clear the screen")
	table_c.add_row("HELP()", "Provide information for client commands")
	console.print(table_c, style="peach", justify="center")



