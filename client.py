from twirp.context import Context
from twirp.exceptions import TwirpServerException

import curency_pb2, curency_twirp

client = curency_twirp.DollarCurencyServiceClient("http://127.0.0.1:3000")

try:
    response = client.GetDollarRate(
    	ctx=Context(), 
        request=curency_pb2.EmptyInput(),
    )
    print(response)
except TwirpServerException as e:
    print(e.code, e.message, e.meta, e.to_dict())
