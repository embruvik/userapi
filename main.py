from fastapi import FastAPI
from pyclient import call_pyserver
from mlclient import call_mlserver
from random import randrange
app = FastAPI()

@app.get("/user/{name}")
async def getUser(name):
    
    fig = {'fig':""}
    r = randrange(0,101)
    if r < 25:
        msg = call_pyserver('greeter', name=name)
    elif r < 50:
        msg = call_pyserver('obsgreeter', name=name)
    else:
        msg = 'see plot'
        fig = call_pyserver('plotter',title=name)

    return {"message": msg, "fig":fig['fig']}

@app.get("/user/ml/{name}")
async def getMlUser(name):
    print('Got request for ML: ',name)
    r = randrange(0,101)
    if r < 25:
        msg = call_mlserver('greeter', name=name, greeting='it works!')
    elif r < 50:
        msg = call_mlserver('obsgreeter', name=name)
    else:
        msg = call_mlserver('plotter',title4plot=name)

    return msg