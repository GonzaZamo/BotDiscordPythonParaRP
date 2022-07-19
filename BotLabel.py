from dis import disco
import discord
from discord import message
from discord.ext import commands
from datetime import date
from urllib import parse, request
import re
import time

from discord.ext.commands.core import Command, bot_has_permissions

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='>>', description="Bot oficial Dream Life RP", intents = intents)
client = discord.Client()
bot.remove_command('help')


@bot.command()
@commands.has_permissions(administrator = True)
async def musculos1(ctx):
    embed = discord.Embed(description="""**Teclas a pie:**
```Chat de texto con todos -------------> T.
Presionar para hablar ---------------> N.
Correr ------------------------------> Shift presionado.
Saltar ------------------------------> Barra Espaciadora.
Ajustar volumen de la voz -----------> º.
Agacharse ---------------------------> Ctrl.
Señalar -----------------------------> B.
Levantar las manos ------------------> X.
Cancelar animaciones ----------------> X.
Caminar hacía adelante --------------> W.
Caminar hacía atrás -----------------> S.
Girar hacía la derecha --------------> D.
Girar hacía la izquierda ------------> A.
Golpear -----------------------------> MB1.
Cambiar de arma ---------------------> Números del 1 al 5.
Abrir el menú Radio IC --------------> F9.
Tirarse al suelo --------------------> U.
Abrir el mapa -----------------------> P ó ESC.
Cruzar los brazos -------------------> G.
Interacción con puntos de trabajo ---> E.
Interacción con puntos de droga -----> E.
Interacción con puntos de compra ----> E.
Interacción para venta de droga Npc -> E.
Cambiar a cámara frontal ------------> C.
Abrir menú de ropa ------------------> ".".
Cambiar zoom de la cámara -----------> V.
Ver/sacar DNI y licencias -----------> "?".
Sacar el teléfono -------------------> F1.
Abrir inventario --------------------> F2.
Menú Animaciones --------------------> F3.
Manú de trabajo ---------------------> F6.
Mostrar facturas --------------------> F7.
Manú de ropa 2 ----------------------> K.
Lista de jugadores en el sv ---------> F10.```""", color=discord.Color.dark_purple())
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    await ctx.send(embed=embed)
    await ctx.message.delete(delay=None)

@bot.command()
@commands.has_permissions(administrator = True)
async def musculos2(ctx):
    embed = discord.Embed(description="""
**Teclas en vehículo:**
```Subirse ----------------------------> F.
Ponerse el cinturón ----------------> K.
Acelerar ---------------------------> W.
Frenar -----------------------------> S.
Girar hacía la derecha -------------> D.
Girar hacía la izquierda -----------> A.
Tomar las llaves -------------------> ",".
Cerrar o abrir el vehículo ---------> ",".
Cambiar estación de radio ----------> "," ó MB3 scroll hacía abajo.
Sacar arma (copiloto) --------------> MB3 scroll hacía arriba.
Abrir el guarda equipaje -----------> L.
Menú del auto ----------------------> Home - Inicio.
Cambiar zoom de la cámara ----------> V.```""", color=discord.Color.dark_purple())
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    await ctx.send(embed=embed)
    await ctx.message.delete(delay=None)

@bot.command()
@commands.has_permissions(administrator = True)
async def musculos3(ctx):
    embed = discord.Embed(description="""
**Comandos en el chat:**
```/ayuda -------> pedir cualquier tipo de ayuda en el servidor.
/ooc ---------> Preguntar cosas fuera de rol (este comando es local).
/report ------> Reportar conflictos o pedir ayuda a la administración.
/auxilio -----> Solicitar servicio a los Ems.
/mecánico-----> Solicitar Servicio de mecánico.```""", color=discord.Color.dark_purple())
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    await ctx.send(embed=embed)
    await ctx.message.delete(delay=None)


@bot.command()
async def help(ctx):
    embed = discord.Embed(description="""
    El bot oficial de Dream Life RP está aquí.
    El prefijo al cual responde el bot oficial de Dream Life RP es \'>>\'.
    Estos son todos los comandos del bot Dream Life RP:
    """, color=discord.Color.dark_purple())
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.add_field(name="➢ __ip__", value="Este comando te muestra la ip del servidor y como acceder al mismo.\n")
    embed.add_field(name="➢ __invitacion__", value="Este comando te muestra la invitación para el servidor de discord.\n")
    embed.add_field(name="➢ __redes__", value="Este comando te indica todas las redes oficiales de Dream Life RP.\n")
    embed.set_footer(text="Si necesitas más ayuda puedes comunicarte con el STAFF de Dream Life RP.")
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")


    #await ctx.send("||@everyone||", embed=embed)
    await ctx.send(embed=embed)
    await ctx.message.delete(delay=None)

@bot.command()
async def redes(ctx):
    embed = discord.Embed(description="""
    **❮ Redes Dream Life RP ❯**

    :boom:  Síguenos en todas nuestras redes sociales para que estés al tanto de Eventos y Sorteos exclusivos :boom:

    :boom: **Facebook** :calling:  https://www.facebook.com/DreamLife-Roleplay-112246511486351

    :boom: **Instagram** :calling: https://www.instagram.com/dreamliferp_es/

    """, color=discord.Color.dark_purple())
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")


    await ctx.send(embed=embed)
    await ctx.message.delete(delay=None)

    # :boom: **Twitter** :calling: https://www.twitter.com/RpMy Life RP

    # :boom: **TikTok** :calling: https://www.tiktok.com/@My Life RP

    # :boom: **Twitch** :calling: https://www.twitch.tv/My Life RP

    # :boom: **YouTube** :calling: https://www.youtube.com/channel/UCOOid5NUj_1LDQdTW1VYi-w





@bot.command()
@commands.has_any_role(947398064308625465, 947398064308625458, 990065298021429350) #Solo Fundadores, Game Master y Administrador
async def reinicio(ctx):
    canal = bot.get_channel(958859081559441478)
    embed = discord.Embed(description=f"""
    ↻ **REINICIO** ↺

    El servidor **Dream Life RP** se encuentra:
    En proceso de **reinicio** si te encuentras en la ciudad usa: **\"f8\"**+**\"quit\"**

    Consulta el canal {canal.mention} para conocer el estado del servidor.
    """, color=discord.Color.gold())
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")
    rol = discord.utils.get(ctx.guild.roles, id=947398064275066953)
    await canal.send(f"||{rol.mention}||", embed=embed)
    # await ctx.send(embed=embed)
    await ctx.message.delete(delay=None)


@bot.command()
@commands.has_any_role(947398064308625465, 947398064308625458, 990065298021429350) #Solo Fundadores, Game Master y Administrador
async def on(ctx):
    canal = bot.get_channel(958859081559441478)
    embed = discord.Embed(description=f"""
    ⋙ **SERVER ON** ⋘

    El servidor **Dream Life RP** se encuentra:
    **Iniciado**, puedes entrar desde FiveM usando:
    **\"f8\"**+**\"connect cfx.re/join/vlqedq\"**

    Consulta el canal {canal.mention} para conocer el estado del servidor.
    """, color=discord.Color.green())
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")
    rol = discord.utils.get(ctx.guild.roles, id=947398064275066953)
    await canal.send(f"||{rol.mention}||", embed=embed)
    # await ctx.send(embed=embed)
    await ctx.message.delete(delay=None)


@bot.command()
@commands.has_any_role(947398064308625465, 947398064308625458, 990065298021429350) #Solo Fundadores, Game Master y Administrador
async def off(ctx):
    canal = bot.get_channel(958859081559441478)
    embed = discord.Embed(description=f"""
    ⋙ **SERVER OFF** ⋘

    El servidor **Dream Life RP** se encuentra:
    En proceso de **mantenimiento**

    Consulta el canal {canal.mention} para conocer el estado del servidor.
    """, color=discord.Color.red())
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")
    rol = discord.utils.get(ctx.guild.roles, id=947398064275066953)
    await canal.send(f"||{rol.mention}||", embed=embed)
    # await ctx.send(embed=embed)
    await ctx.message.delete(delay=None)


@bot.command()
async def ip(ctx):
    canal = bot.get_channel(977343070490218537)
    embed = discord.Embed(description=f"""
    **❮ IP ❯**

    IP: **connect cfx.re/join/vlqedq**
    En FiveM utiliza: **\"f8\"** + **IP**

    Si no te deja, levanta un ticket de soporte general en
    {canal.mention} y Soporte técnico te ayudará

    """, color=discord.Color.dark_purple())
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")


    await ctx.send(embed=embed)
    await ctx.message.delete(delay=None)


@bot.command()
async def invitacion(ctx):
    await ctx.message.delete(delay=None)
    embed = discord.Embed(description="""
    **❮ INVITACIÓN ❯**

Para invitar a cualquier amigo a rolear en nuestro servidor solo envíale este enlace: ****

""", color=discord.Color.dark_purple())
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")
    await ctx.send(embed=embed)


@bot.command()
async def aprobadow(ctx, user: discord.Member):
    await ctx.message.delete(delay=None)
    role = discord.utils.get(user.guild.roles, id=947398064275066954)
    embed = discord.Embed(description = f"""
**❮ WL APROBADA ❯**

Enhorabuena {user.mention}, has conseguido aprobar tu entrevista de whitelist satisfactoriamente, siempre respeta la normativa y tu interpretación de personaje.
Disfruta de tu estadía en la ciudad.

Cualquier duda que tengas puedes pedirle ayuda a cualquier miembro del **staff de Dream Life RP**.

    """, color = discord.Color.green())
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")
    await ctx.send(embed = embed)
    await user.add_roles(role)



@bot.command()
async def reprobadow(ctx, user: discord.Member, numero):
    if numero == '1':
        tiempo = "24 horas"
        role = discord.utils.get(user.guild.roles, id=953515745004904459)
    if numero == '2':
        tiempo = "3 días"
        role = discord.utils.get(user.guild.roles, id=953515791603626035)
    if numero == '3':
        tiempo = "7 días, de reprobar nuevamente no podrás ingresar a ninguna facción whitelist durante un mes completo"
        role = discord.utils.get(user.guild.roles, id=953515822180098048)
    fecha = date.today()
    await ctx.message.delete(delay=None)
    embed = discord.Embed(title = "Dream Life RP®", description = f"""
**❮ WHITELIST REPROBADA ❯**

Lo siento {user.mention}, no has conseguido aprobar tu entrevista de whitelist, repasa la normativa un poco más y vuelve a pedirla dentro de {tiempo}.

Cualquier duda que tengas puedes pedirle ayuda a cualquier miembro del **staff de Dream Life RP**.

    """, color = discord.Color.red())
    embed.set_author(name=f"{ctx.author.display_name}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")
    embed.set_footer(text = f"{fecha}")
    channel = bot.get_channel(953514427016179723)
    await channel.send(embed = embed)
    await user.add_roles(role)


@bot.command()
async def aprobadoh(ctx, user: discord.Member):
    await ctx.message.delete(delay=None)
    role = discord.utils.get(user.guild.roles, id=947433501525934140)
    embed = discord.Embed(description = f"""
**❮ HISTORIA APROBADA ❯**

Enhorabuena {user.mention}, la historia de tu personaje ha sido aceptada, puedes pedir tu entrevista para la whitelist en el canal respectivo.

Cualquier duda que tengas puedes pedirle ayuda a cualquier miembro del **staff de Dream Life RP**.
    """, color = discord.Color.green())
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")
    await ctx.send(embed = embed)
    await user.add_roles(role)



@bot.command()
async def reprobadoh(ctx, user: discord.Member):
    fecha = date.today().strftime('%d/%m/%Y')
    await ctx.message.delete(delay=None)
    embed = discord.Embed(title = "Dream Life RP®", description = f"""
**❮ HISTORIA REPROBADA ❯**

Lo siento {user.mention}, tu historia no ha sido aprobada, te recomendamos revisarla y mejorarla según los requerimientos necesarios..

Cualquier duda que tengas puedes pedirle ayuda a cualquier miembro del **staff de Dream Life RP**.

    """, color = discord.Color.red())
    embed.set_author(name=f"{ctx.author.display_name}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")
    embed.set_footer(text = f"{fecha}")
    channel = bot.get_channel(953514427016179723)
    await channel.send(embed = embed)


@bot.command()
async def aprobadoe(ctx, user: discord.Member, fac):
    await ctx.message.delete(delay=None)
    canal = bot.get_channel(953529673076322344)
    if fac == 'meca':
        role = discord.utils.get(user.guild.roles, id=953529930002624563)
        faccion1 = '**Mecánicos**'
        imagen = "https://cdn.discordapp.com/attachments/720790443670896772/876521638231965727/Comp_3_00002.png"
        faccion = 'Contáctate con alguien de la jefatura de **Mecánicos** para que te de tu rango dentro del servidor de la facción y se pongan de acuerdo para que de manera IC vayas a realizar una \"entrevista de trabajo\".'
        await user.send("Te esperamos en discord para darte el trabajo: (Aquí va la invitación al discord de mecas)")

    elif fac == 'ems':
        role = discord.utils.get(user.guild.roles, id=953530727872483338)
        faccion1 = '**EMS**'
        imagen = "https://cdn.discordapp.com/attachments/720790443670896772/876521634280902726/Comp_3_00000.png"
        faccion = 'Contáctate con alguien de la jefatura de **EMS** para que te de tu rango dentro del servidor de la facción y se pongan de acuerdo para que de manera IC vayas a realizar una \"entrevista de trabajo\".'
        await user.send("Te esperamos en discord para darte el trabajo: (Aquí va la invitación al discord de ems)")

    elif fac == 'pol':
        role = discord.utils.get(user.guild.roles, id=953530623648210974)
        faccion1 = '**Policía**'
        imagen = "https://cdn.discordapp.com/attachments/720790443670896772/876521645496471592/Comp_3_00007.png"
        faccion = 'Contáctate con alguien de la jefatura de **Policía** para que te de tu rango dentro del servidor de la facción y se pongan de acuerdo para que de manera IC vayas a realizar una \"entrevista de trabajo\".'
        await user.send("Te esperamos en discord para darte el trabajo: (Aquí va la invitación al discord de polis)")

    elif fac == 'myb':
        role = discord.utils.get(user.guild.roles, id=953530995108372530)
        faccion1 = '**Mafias y Bandas**'
        imagen = "https://cdn.discordapp.com/attachments/720790443670896772/876540097175109652/Comp_1_00001.png"
        faccion = 'Por favor levanta un ticket ilicito para que alguien del staff te brinde el enlace al discord de **mafias y bandas** y se les brinde el rol de \"Whitelist M&B\"'
        await user.send("Te esperamos en discord para darte tu rango: (Aquí va la invitación al discord de mafias y bandas)")
    embed = discord.Embed(title = "Dream Life RP®", description = f"""
**❮ ENTREVISTA APROBADA ❯**

Enhorabuena {user.mention}, has conseguido aprobar satisfactoriamente tu entrevista de {faccion1}, recuerda respetar siempre las normativas.

_{faccion}_

Cualquier duda que tengas puedes pedirle ayuda a cualquier miembro del **staff de Dream Life RP**.
    """, color = discord.Color.green())
    embed.set_author(name=f"{ctx.author.display_name}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=imagen)
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")
    await canal.send(embed = embed)
    await user.add_roles(role)


@bot.command()
async def reprobadoe(ctx, user: discord.Member, fac):
    await ctx.message.delete(delay=None)
    channel = bot.get_channel(953529673076322344)
    if fac == 'meca':
        faccion = '**Mecánicos**'
        imagen = "https://cdn.discordapp.com/attachments/720790443670896772/876521638231965727/Comp_3_00002.png"
        canal = 953536483795558430
    elif fac == 'ems':
        faccion = 'EMS'
        imagen = "https://cdn.discordapp.com/attachments/720790443670896772/876521634280902726/Comp_3_00000.png"
        canal = 947409282352168971
    elif fac == 'pol':
        faccion = 'Policía'
        imagen = "https://cdn.discordapp.com/attachments/720790443670896772/876521645496471592/Comp_3_00007.png"
        canal = 947409211694911528
    elif fac == 'myb':
        faccion = 'Mafias y Bandas'
        imagen = "https://cdn.discordapp.com/attachments/720790443670896772/876540097175109652/Comp_1_00001.png"
        canal = 947580584014786593
    embed = discord.Embed(title = "Dream Life RP RP®", description = f"""
**❮ ENTREVISTA REPROBADA ❯**

Lo siento {user.mention}, no has conseguido aprobar tu entrevista de **{faccion}**, por favor repasa más la normativa de {faccion}.

Recuerda que tienes que esperar hasta mañana para realizar de nuevo tu oposición.
En caso que sea tu segunda oposición, tendrás que esperar hasta que vuelvan a abrir opociónes para la facción.
Puedes consultar eso en el canal <#{canal}>

Cualquier duda que tengas puedes pedirle ayuda a cualquier miembro del **staff de Dream Life RP**.
    """, color = discord.Color.red())
    embed.set_author(name=f"{ctx.author.display_name}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=imagen)
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")
    await channel.send(embed = embed)





@bot.command()
# @commands.has_any_role(867312511962054686, 867310961715445761)
async def normativa(ctx):
   await ctx.message.delete(delay=None)
   embed = discord.Embed(description="""
   ❮ NORMATIVAS DREAM LIFE RP❯
   """, color=discord.Color.dark_purple())
   embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
   embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
   embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")

   await ctx.send(embed=embed)


@bot.command()
async def banner(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")
    await ctx.message.delete(delay=None)


@bot.command()
async def updates(ctx, *, updates):
    await ctx.message.delete(delay=None)
    embed = discord.Embed(description=f"""**
-----------------------------**

{updates}

Cualquier duda que tengas puedes levantar un ticket de **Soporte General** en <#977343070490218537>
**-----------------------------
**""", color=discord.Color.dark_purple())
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")

    rol = discord.utils.get(ctx.guild.roles, id=947398064275066953)
    await ctx.send(f"||{rol.mention}||", embed=embed)


@bot.command()
async def myb(ctx):
    canal = 867309846965256212
    embed = discord.Embed(description=f"""
**❮ POSTULACIONES MAFIAS/BANDAS ❯**
Buenas ciudadano, ¿Le tienes rencor a la policía, lo legal no es lo tuyo, te llama la atención el mundo ilícito?
Las **Bandas, mafias y carteles** son los indicados para ti, tendrás diferentes robos disponibles, armamento respectivo al alcance, mucha adrenalina huyendo de la ley y realizando todos los actos ilícitos que desees.

**Para solicitar tu whitelist de Mafias y Bandas solicita tu entrevista en <#{canal}>**
Siempre y cuando tengas los siguientes requisitos:
•    Ser Mayor de 15 años OOC.
•    Historia de la banda, mafia o cartel, así como de cada miembro.
•    No tener sanciones administrativas graves.
•    **Cada miembro** con Whitelist aprobado al menos 3 días después de aprobada la historia.
""", color=discord.Color.dark_purple())
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/720790443670896772/876540097175109652/Comp_1_00001.png")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")


    await ctx.send('||@everyone||', embed=embed)
    await ctx.message.delete(delay=None)


@bot.command()
async def ems(ctx):
    canal = 867309846965256212
    embed = discord.Embed(description=f"""
**❮ POSTULACIONES EMS ❯**
Buenas ciudadano, ¿te interesa apoyar a la ciudadanía, salvar vidas, y tener buena experiencia laboral?
La EMS es la indicada para ti, tendrás buena paga y un excelente equipo de trabajo lleno de actitud y alegría.

**Para solicitar tu whitelist de EMS solicita tu entrevista en <#{canal}>**""", color=discord.Color.dark_purple())
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/720790443670896772/876521634280902726/Comp_3_00000.png")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")


    await ctx.send('||@everyone||', embed=embed)
    await ctx.message.delete(delay=None)


@bot.command()
async def pol(ctx):
    canal = 867309846965256212

    embed = discord.Embed(description=f"""
**❮ POSTULACIONES LAPD ❯**
Buenas ciudadano, ¿te interesa hacer investigaciones, salvaguardar la vida de los ciudadanos, asistir a los diferentes atracos dentro de la ciudad?
La LAPD es la indicada para ti, aparte de pagas semanales, obtendrás un bono extra dependiendo tu rendimiento durante cada semana.

**Para solicitar tu whitelist de LAPD solicita tu entrevista en <#{canal}>**
Siempre y cuando tengas los siguientes requisitos:
•    Ser Mayor de 16 años OOC.
•    Ser mayor de 20 años IC
•    No tener sanciones administrativas graves.
•    No tener antecedentes de grado medio o superior""", color=discord.Color.dark_purple())
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/720790443670896772/876521645496471592/Comp_3_00007.png")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")

    await ctx.send("||@everyone||", embed=embed)
    await ctx.message.delete(delay=None)


@bot.command()
async def meca(ctx):
    canal = 867309846965256212

    embed = discord.Embed(description=f"""
**❮ POSTULACIONES MECÁNICOS ❯**
Buenas ciudadano, ¿te interesan los coches, mejorar su motor al máximo, modificarles la pintura y realizar toonings?
Los **mecánicos** somos los indicados para ti, aparte de pagas semanales, obtendrás un bono extra dependiendo tu rendimiento durante cada semana.

**Para solicitar tu whitelist de Mecánicos solicita tu entrevista en <#{canal}>**
""", color=discord.Color.dark_purple())
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/720790443670896772/876521638231965727/Comp_3_00002.png")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")

    await ctx.send("||@everyone||", embed=embed)
    await ctx.message.delete(delay=None)


@bot.command()
async def discords(ctx):
    await ctx.message.delete(delay=None)
    embed = discord.Embed(description = f"""
**❮ Discords Dream Life RP ❯**

•    **_Dream Life RP_**
https://discord.gg

•    **_Dream Life RP Police Department_**
https://discord.gg

•    **_IMSS_**
https://discord.gg

•    **_Mecánicos_**
https://discord.gg

•    **_Mafias y Bandas_**
https://discord.gg

•    **_Policía Federal_**
https://discord.gg

•    **_Benny's_**
https://discord.gg

•    **_Abogados_**
https://discord.gg

•    **_Crayolita Bakery_**
https://discord.gg

•    **_Mosley's_**
https://discord.gg

•    **_Tequila-La_**
https://discord.gg

•    **_Galaxy_**
https://discord.gg

•    **_Casino_**
https://discord.gg

•    **_Bahamas_**
https://discord.gg

•    **_Vanilla_**
https://discord.gg

•    **_Merryweather_**
https://discord.gg

•    **_FBI_**
https://discord.gg

    """, color = discord.Color.dark_purple())
    embed.set_author(name=f"{ctx.guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")
    await ctx.send("@everyone", embed = embed)


@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.message.delete(delay=None)
    if reason is None: # If the moderator did not enter any reason.# This command sends message in the channel for confirming BAN!
        await ctx.send(f"{member.mention} Has sido baneado del servidor\nPor no cumplir las normativas con el servidor")
        await member.send(f"""Fuiste baneado de **Dream Life RP** por no cumplir la normativa requerida para la comunidad
    Si crees que es injusto entra a este discord para apelarlo: (invitacion a discord)
    Te desamos lo mejor dentro del roleplay GTAV, agradecemos tu tiempo de calidad dentro de Dream Life RP y lamentamos haber llegado a esta situación.""")
        await ctx.guild.ban(member, reason = reason) # Bans the member.

    else: # If the moderator entered a reason.# This command sends message in the channel for confirming BAN!
        await ctx.send(f"{member.mention} Has sido baneado del servidor\nPor {reason}")
        await member.send(f"""Fuiste baneado de **Dream Life RP** por {reason}
    Si crees que es injusto entra a este discord para apelarlo: (invitacion a discord)
    Te desamos lo mejor dentro del roleplay GTAV, agradecemos tu tiempo de calidad dentro de Dream Life RP y lamentamos haber llegado a esta situación.""")
#        await ctx.guild.ban(member, reason = reason) # Bans the member.


@bot.command()
async def anun(ctx, *, anuncio):
    embed = discord.Embed(description = f"""

{anuncio}

""", color = discord.Color.dark_purple())
    embed.set_author(name = f"{ctx.guild.name}®", icon_url = f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")
    await ctx.send(embed=embed)
    await ctx.message.delete(delay=None)


@bot.command()
async def anuncio(ctx, *, anuncio):
    await ctx.send(anuncio)
    await ctx.message.delete(delay=None)


@bot.command()
async def staffaceptado(ctx, user: discord.Member, rango):
    await ctx.message.delete(delay=None)
    channel = bot.get_channel(947398065743093813)
    rol = discord.utils.get(user.guild.roles, id=947398064291856435)
    if rango == "soporte":
        role = discord.utils.get(user.guild.roles, id=947398064291856442)
        await user.send(f"Has sido aceptado como **soporte** dentro del staff de Dream Life RP")
        await user.add_roles(role)
    if rango == "entrevistador":
        role = discord.utils.get(user.guild.roles, id=947419010595708928)
        await user.send(f"Has sido aceptado como **entrevistador** dentro del staff de Dream Life RP")
        await user.add_roles(role)
    if rango == "CM":
        role = discord.utils.get(user.guild.roles, id=947398064291856439)
        await user.send(f"Has sido aceptado como **comunity manager** dentro del staff de Dream Life RP")
        await user.add_roles(role)
    if rango == "mod":
        role = discord.utils.get(user.guild.roles, id=947398064291856443)
        await user.send(f"Has sido aceptado como **moderador** dentro del staff de Dream Life RP")
        await user.add_roles(role)
    await user.add_roles(rol)
    embed = discord.Embed(description = f"""
{ctx.author.mention} ha aprobado en el {rol.mention} a {user.mention} como {role.mention}
""", color=discord.Color.dark_purple())
    embed.set_author(name=f"{ctx.guild.name}®",icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
    await channel.send(embed=embed)


@bot.command()
async def sugerencia(ctx, *, sug):
    ch = bot.get_channel(947400236144406529)
    if ctx.channel != ch:
        await ctx.message.delete(delay=None)
        await ctx.send(f"{ctx.author.mention} Por favor, envía ese mensaje en el apartado de {ch.mention}")
    if ctx.channel == ch:
        embed = discord.Embed(description = f"""
**SUGERENCIA POR PARTE DE** {ctx.author.name}
{sug}
""", color = discord.Color.dark_purple())
        embed.set_author(name = f"{ctx.guild.name}®", icon_url = f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
        embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
        await ctx.message.delete(delay=None)
        Moji = await ctx.send(embed=embed)
        await Moji.add_reaction(emoji = '✅')
        await Moji.add_reaction(emoji = '❎')



@bot.command()
async def bug(ctx, *, bug):
    await ctx.message.delete(delay=None)
    ch = bot.get_channel(977387627076538368)
    if ctx.channel != ch:
        await ctx.send(f"{ctx.author.mention} Por favor, envía ese mensaje en el apartado de {ch.mention}")
    if ctx.channel == ch:
        embed = discord.Embed(description = f"""
**BUG REPORTADO POR** {ctx.author.name}
{bug}
""", color = discord.Color.dark_purple())
        embed.set_author(name = f"{ctx.guild.name}®", icon_url = f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
        embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
        Moji = await ctx.send(embed=embed)
        await Moji.add_reaction(emoji = '✅')


@bot.command()
async def warn(ctx, user: discord.Member, num = None, *, reason = None):
    await ctx.message.delete(delay=None)
    ch = bot.get_channel(953854115287531550)
    if num == '3':
        if user.roles(953849687352442930):
            role = discord.utils.get(user.guild.roles, id=953849778029101128)
            text = "Tienes dos strikes, por favor ya deja de cometer faltas, el siguiente es motivo de ban."
        if user.roles(953849778029101128):
            role = discord.utils.get(user.guild.roles, id=953850027112017970)
            text = "Has sido baneado permanentemente del servidor de manera IC, puedes apelarlo abriendo un ticket."
        else:
            role = discord.utils.get(user.guild.roles, id=953849687352442930)
            text = "Tienes un strike, no sigas cometiendo faltas."
    if num == None or num == '1':
        role = discord.utils.get(user.guild.roles, id=953849242273865758)
        text = "Tienes un primer warn, recuerda que cada 3 warns se te aplicará un strike no acumules muchos."
    if num == '2':
        role = discord.utils.get(user.guild.roles, id=953849431265013770)
        text = "Tienes un segundo warn, el siguiente será un strike más acumulado."

    await user.add_roles(role)
    await user.send(f"{text}")
    if reason == None:
        description = f"El usuario {user.mention} fue sancionado con {role} por el miembro del staff {ctx.author.mention}."
    if reason != None:
        description = f"El usuario {user.mention} fue sancionado con {role.mention} por el miembro del staff {ctx.author.mention} con la razón: {reason}."
    embed = discord.Embed(description = description, color = discord.Color.dark_purple())
    embed.set_author(name = f"{ctx.guild.name}®", icon_url = "https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
    embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
    await ch.send(embed=embed)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(977342375988977716)
    ch = bot.get_channel(947398064325427282)
    embed=discord.Embed(
        title=f"¡Bienvenido {member.name}!",
        description="Por favor Lee las normativas del servidor y respeta a los demás.",
        color=discord.Color.dark_purple())
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")
    await channel.send(f"""**Canal de normativas: {ch.mention}.**
{member.mention} Recuerda respetarlas siempre.""" , embed = embed)
    contador = bot.get_channel(953485581827051620)
    await contador.edit(name = '📊︲Miembros: {}'.format(channel.guild.member_count))


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(977342375988977716)
    ch = bot.get_channel(953499248295559208)
    text = f"Nos vemos en otra {member.name}!"
    await ch.send(text)
    contador = bot.get_channel(953485581827051620)
    await contador.edit(name = '📊︲Miembros: {}'.format(channel.guild.member_count))


@bot.event
async def on_raw_reaction_add(payload):  # Requires Intents.reactions
    guild = bot.get_guild(payload.guild_id)
    role = discord.utils.get(guild.roles, id=947398064275066953)

    if payload.message_id == 988285697565802556:
        if str(payload.emoji) == "✅":
            await payload.member.add_roles(role, atomic=True)


@bot.command()
async def clchannel(ctx):
    await ctx.message.delete(delay=None)
    async for msg in ctx.channel.history(limit=None):
        await msg.delete(delay=None)



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Dream Life RP", url="http://www.twitch.tv/lvpes2"))

    # MENSAJE DE VERIFICACION
#     guild = bot.get_guild(947398064275066951)
#     Channel = bot.get_channel(947398065902452812)
#     embed = discord.Embed(description="""
#     **❮ VERIFICACIÓN ❯**

# Para verificarte como ciudadano de Dream Life RP reacciona a este mensaje.

# """, color=discord.Color.from_rgb(0, 0, 0))
#     embed.set_author(name=f"{guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
#     embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
#     embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")
#     Moji = await Channel.send(embed = embed)
#     await Moji.add_reaction(emoji = '✅')

#     # MENSAJE DE SUGERENCIA
#     guild = bot.get_guild(947398064275066951)
#     Channel = bot.get_channel(977387627076538368)
#     embed = discord.Embed(description="""
#     **❮ BUGS ❯**

# Para enviar los bugs encontrados usa el comando **>>bug + {tu bug}.**""", color=discord.Color.from_rgb(0, 0, 0))
#     embed.set_author(name=f"{guild.name}®", icon_url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
#     embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/920462101909217290/976252463298527292/logo_animacion_2.gif")
#     embed.set_image(url = "https://cdn.discordapp.com/attachments/920462101909217290/976250103687966770/banner-fivemv2.gif")
#     await Channel.send(embed = embed)

bot.run()#Token del bot entre comillas y dentro del paréntesis