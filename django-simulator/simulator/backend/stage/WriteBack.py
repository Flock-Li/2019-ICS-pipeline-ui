from simulator.backend.const import*

def WriteBack(now,nextp,reg):
    reg.writeregister(now.W[dstE] ,now.W[valE], now.W[dstM], now.W[valM])