#kick
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def kick(ctx, member: discord.Member, *, reason = None):
    emb = discord.Embed(title = 'Кик', colour = discord.Color.green() )
    await ctx.channel.purge(limit = 1)
    await member.kick(reason=reason)
    emb.set_author(name = member.name, icon_url= member.avatar.url)
    emb.add_field(name = 'Кик', value = 'кикнул игрока : {}'.format(member.mention))
    emb.set_footer(text = 'Был кикнут администратором {}'.format(ctx.author.name), icon_url = ctx.author.avatar.url)
    await ctx.send( embed= emb)
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1 )