
from mcdreforged.api.all import *
from time import sleep
remind_message='''
§9§l检测到您的网络ipv4访问优先
§9§l如果为家庭网络请检查路由器/光猫是否开启ipv6模式
'''

def on_player_joined(server: PluginServerInterface, player: str, info: Info):

	ip_len = info.content.find(']')-info.content.find('[')
	if ip_len < 25 and ip_len>5:
		sleep(1)
		server.tell(player,remind_message)
	
	



