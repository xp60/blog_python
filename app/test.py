import asyncio

import orm

from models import User,Blog,Comment

async def test(loop):

    await orm.create_pool(loop,user='root', password='123', db='awesome',host='127.0.0.1')

    u = User(id='02',name='song', email='test@example.com',admin=False, passwd='1234567890', image='about:blank',create_at=0.2)

    await u.save()

if __name__ == '__main__':

    loop = asyncio.get_event_loop()

    loop.run_until_complete(test(loop))

    print('test finished')

    loop.close()