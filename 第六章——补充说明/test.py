from flask import Flask,render_template
import pandas as pd
a=pd.read_csv("")
a.rename(columns={"2":"3","3":"4"})
a.to_dict()