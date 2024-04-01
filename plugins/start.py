from pyrogram import Client , filters
import imdb
from pyrogram.types import Message, ReplyKeyboardMarkup , ReplyKeyboardRemove  ,InputTextMessageContent,InlineKeyboardMarkup , InlineKeyboardButton , InlineQuery , CallbackQuery, InlineQueryResultArticle, InlineQueryResult

ia = imdb.IMDb()

@Client.on_message(filters.command('start'))
async def start(client = Client ,message =  Message):
     await message.reply_text(text='hi welcom' , reply_markup=InlineKeyboardMarkup(
                        [
                             [
                        InlineKeyboardButton('search' , switch_inline_query_current_chat= '')
                             ]
                        ]
                         
                         )
                        )
     

def search_movies(query):
    return ia.search_movie(query)


@Client.on_inline_query()
async def search(_ , query):
     results = []
     movie = search_movies(query.query)
     
     for i, content in enumerate(movie):
        result = InlineQueryResultArticle(
            id=str(i),
            title=str(content),
            input_message_content=InputTextMessageContent(f"""
                                                          Movie: {str(movie[i]['title'])} , {str(movie[i]['year'])}  {ia.get_imdbURL(content)}
                                                          """),
        )
        results.append(result)
     await query.answer(results)


     




