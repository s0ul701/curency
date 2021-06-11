from decimal import Decimal
from xml.etree import ElementTree

from aiohttp import ClientSession
from twirp.asgi import TwirpASGIApp

import curency_pb2, curency_twirp


class DollarCurencyService:
    DOLLAR_CURENCY_URL = 'https://www.cbr.ru/scripts/XML_daily.asp'
    DOLLAR_CHARS = 'USD'

    async def GetDollarRate(self, context, empty):
        async with ClientSession() as session:
            async with session.get(self.DOLLAR_CURENCY_URL) as response:
                response_body = await response.text()
                for curency in ElementTree.fromstring(response_body):
                    if curency[1].text == self.DOLLAR_CHARS:
                        return curency_pb2.DollarCurency(
                            rubles=Decimal(curency[4].text.replace(',', '.')),
                        )
                return curency_pb2.DollarCurency(rubles=Decimal(-1))


service = curency_twirp.DollarCurencyServiceServer(
    service=DollarCurencyService()
)
app = TwirpASGIApp()
app.add_service(service)
