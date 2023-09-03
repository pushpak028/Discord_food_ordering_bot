from discord import Intents , Client , Message
from discord.ext import commands
import response
import load_json
from importlib import reload
reload(response)

def app_run(token):
    intents = Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix='!',intents=intents)
    kb:dict = load_json.load1("dish_name.json")

    orders = {}

    @client.event
    async def on_ready():
        print(f"{client.user} is now running ")
        channel_id = "your-channel_id"
        channel = client.get_channel(channel_id)
        
        tags = [i["name"] for i in kb]
        butler = "butler: please enter the food name mentioned below using !add_item [item]"
        commands_tobe = ["!start_order","!add_item","view_order","place_order"]
        await channel.send(commands_tobe)
        await channel.send(butler)
        await channel.send(tags)
    
    @client.command()
    async def start_order(ctx):

        orders[ctx.author.id] = []
        await ctx.send("butler: Your order is started , You can add the order by typing '!add_item [name]' ")
    
    @client.command()
    async def add_item(ctx,item):
        
        if ctx.author.id in orders:

            if item.lower() in [i["name"].lower() for i in kb]:
                orders[ctx.author.id].append(item)
                await ctx.send("butler: order added successfully")
            else:
                await ctx.send("butler: Currently dish is unavailable please try some other dish")
        
        else:
            await ctx.send("butler: please start the order using '!start_order")
    
    @client.command()
    async def view_order(ctx):

        if ctx.author.id in orders:
            user_order = orders[ctx.author.id]
            if user_order:
                await ctx.send(user_order)
            else:
                await ctx.send("butler: your order is empty")
        else:
            await ctx.send("butler: please start the order using '!start_order")
    
    @client.command()
    async def place_order(ctx):

        if ctx.author.id in orders:
            user_order = orders[ctx.author.id]

            if user_order:
                price = []

                for i in user_order:
                    for j in kb:
                        if i.lower() == j["name"].lower():
                            price.append(j["price"])
                
                amount = sum(price)

                await ctx.send(amount)
                await ctx.send(price)
            
            else:

                await ctx.send("butler: your order is empty")
        else:
            await ctx.send("butler: please start the order using '!start_order")
    

    client.run(token=token)

                
if __name__ == "__main__":
    app_run("your-token")

            


    




                

            
        