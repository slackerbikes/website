from django.shortcuts import render
from crover.models import graph
import pickle
import io,base64

import matplotlib.cm as cm

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def convert(field):
    np_bytes = base64.b64decode(field)
    return pickle.loads(np_bytes)

# def generateColours(t):
#     minimum,maximum = np.min(t),np.max(t)
#     coolwarm = cm = plt.get_cmap('coolwarm') 
#     cNorm = colors.Normalize(vmin=minimum,vmax=maximum)
#     scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=coolwarm)
#     return scalarMap

def generateGraph(x,y,t):
    fig,ax = plt.subplots(figsize=(12,8))
    sp = ax.scatter(x,y,s=t,alpha=1,c=t,cmap=cm.coolwarm)
    ax.set_xlabel(r'x_position', fontsize=15)
    ax.set_ylabel(r'y_position', fontsize=15)
    ax.set_title('Location & Health of Silo')
    ax.grid(True)

    fig.colorbar(sp)
    # ax.pcolormesh(t,cmap='coolwarm')
    
    flike = io.BytesIO()
    fig.savefig(flike)
    b64 = base64.b64encode(flike.getvalue()).decode()
    return b64

def graphChoice(request):
    choices = graph.objects.all()
    context_dict = {}
    titles = []

    for choice in choices:
        titles.append(choice.title)
        context_dict['choices'] = titles

    return render(request,'crover/selection.html',context=context_dict)


def index(request,name):
    choices = graph.objects.all()
    context_dict = {}

    titles = []
    for choice in choices:
        titles.append(choice.title)
        context_dict['choices'] = titles

    g = graph.objects.get(title=name)
    x,y,t = convert(g.x),convert(g.y),convert(g.temperature)

    # context_dict = {'silo':g,'x':x,'y':y,'t':t}
    context_dict['chart'] = generateGraph(x,y,t)

    return render(request,'crover/graph.html',context=context_dict)

