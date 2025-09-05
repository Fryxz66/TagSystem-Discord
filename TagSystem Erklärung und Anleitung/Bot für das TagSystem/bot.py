import discord
from discord import app_commands
from dotenv import load_dotenv
import os

# Lade den Token aus der .env-Datei
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

# Bot initialisieren mit Intents
intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

# Variable für die erlaubte Rolle
allowed_role_id = 1411490060636782612

@bot.event
async def on_ready():
    print(f'Bot ist online als {bot.user}!')
    # Synchronisiere Slash-Commands mit dem Server
    await tree.sync()
    print('Slash-Commands synchronisiert.')

# Slash-Command: Erlaubte Rolle festlegen (nur für Admins)
@tree.command(name='set_allowed_role', description='Setzt die Rolle, die den Bot nutzen darf.')
@app_commands.default_permissions(administrator=True)  # Nur Nutzer mit "Administrator"
async def set_allowed_role(interaction: discord.Interaction, role: discord.Role):
    global allowed_role_id
    allowed_role_id = role.id
    await interaction.response.send_message(f'Die erlaubte Rolle wurde auf {role.name} gesetzt. Nur Nutzer mit dieser Rolle können den Bot nutzen.')

# Hilfsfunktion: Prüft, ob der User die erlaubte Rolle hat
async def check_allowed_role(interaction: discord.Interaction):
    if allowed_role_id is None:
        await interaction.response.send_message('Keine erlaubte Rolle festgelegt. Verwende /set_allowed_role zuerst.')
        return False
    if interaction.user.get_role(allowed_role_id) is None:
        await interaction.response.send_message('Du hast keine Berechtigung, diesen Bot zu nutzen.')
        return False
    return True

# Slash-Command: Rolle hinzufügen
@tree.command(name='add_role', description='Fügt einem Nutzer eine Rolle hinzu.')
@app_commands.default_permissions(manage_roles=True)  # Benötigt "Manage Roles"
async def add_role(interaction: discord.Interaction, member: discord.Member, role: discord.Role):
    if not await check_allowed_role(interaction):
        return
    if role in member.roles:
        await interaction.response.send_message(f'{member.name} hat die Rolle {role.name} bereits.')
        return
    if role.position >= interaction.guild.me.top_role.position:
        await interaction.response.send_message('Ich kann diese Rolle nicht vergeben, da sie höher oder gleich meiner höchsten Rolle ist.')
        return
    await member.add_roles(role)
    await interaction.response.send_message(f'Rolle {role.name} wurde zu {member.name} hinzugefügt.')

# Slash-Command: Rolle entfernen
@tree.command(name='remove_role', description='Entfernt eine Rolle von einem Nutzer.')
@app_commands.default_permissions(manage_roles=True)  # Benötigt "Manage Roles"
async def remove_role(interaction: discord.Interaction, member: discord.Member, role: discord.Role):
    if not await check_allowed_role(interaction):
        return
    if role not in member.roles:
        await interaction.response.send_message(f'{member.name} hat die Rolle {role.name} nicht.')
        return
    if role.position >= interaction.guild.me.top_role.position:
        await interaction.response.send_message('Ich kann diese Rolle nicht entfernen, da sie höher oder gleich meiner höchsten Rolle ist.')
        return
    await member.remove_roles(role)
    await interaction.response.send_message(f'Rolle {role.name} wurde von {member.name} entfernt.')

# Fehlerbehandlung für Slash-Commands
@tree.error
async def command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message('Du hast keine Berechtigung, diesen Command auszuführen. Bitte kontaktiere einen Admin.')
    elif isinstance(error, app_commands.CommandInvokeError):
        await interaction.response.send_message('Fehler: Ungültiger User oder Rolle. Verwende: /add_role @user @role')
    else:
        await interaction.response.send_message(f'Fehler: {error}')

# Bot starten

bot.run(TOKEN)
