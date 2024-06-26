from pyrogram import Client , filters
import imdb
from pyrogram.types import Message, ReplyKeyboardMarkup , ReplyKeyboardRemove  ,InputTextMessageContent,InlineKeyboardMarkup , InlineKeyboardButton , InlineQuery , CallbackQuery, InlineQueryResultArticle, InlineQueryResult

# Proxy = { "scheme": "socks5",
# "hostname": "0.0.0.0",
# "port": 10000}

app = Client( "test_bot",
             # proxy = Proxy,
             api_id =  ,
             api_hash = "" ,
             bot_token = "6932883798:AAGpel6pNCE8Kug38MIV0o7v4kTCmYlBSwc")


ia = imdb.IMDb()

@app.on_message(filters.command('start'))
async def start(client = Client ,message =  Message):
     await message.reply_text(text='hey start searching' , reply_markup=InlineKeyboardMarkup(
                        [
                             [
                        InlineKeyboardButton('search' , switch_inline_query_current_chat= '')
                             ]
                        ]
                         
                         )
                        )
     

def search_movies(query):
    return ia.search_movie(query)


@app.on_inline_query()
async def search(_ , query):
     results = []
     movie = search_movies(query.query)
     
     for i, content in enumerate(movie):
        result = InlineQueryResultArticle(
            id=str(i),
            title=str(content),
            input_message_content=InputTextMessageContent(f"""
                                                          Movie: {str(movie[i]['title'])}
                                                          {ia.get_imdbURL(content)}
                                                          """),
        )
        results.append(result)
     await query.answer(results)


     






app.run()
