import matplotlib.pyplot as plt
import pandas as pd
def evaluate(hist):
    pd.DataFrame(hist.history).plot()
    plt.ylabel("Loss")
    plt.xlabel("epoches")
