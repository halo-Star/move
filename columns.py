#!/usr/bin/env python
# coding: utf-8

# In[15]:


import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import dash_reusable_components as drc
import dash_bootstrap_components as dbc


# In[39]:


import pandas as pd
test=pd.read_csv("test_file.csv")
flag=0
app = dash.Dash()
app.layout=dbc.Form(id="form",children=
    [
        dbc.FormGroup(
            [
                drc.NamedDropdown(
                    name='A',
                    id='dropdown-layout-1',
                    options=drc.DropdownOptionsList(*list(test.columns)),
                    value=None,
                    clearable=False
                )
            ],
            className="mr-3",
        ),
        dbc.FormGroup(
            [
                drc.NamedDropdown(
                    name='B',
                    id='dropdown-layout-2',
                    options=drc.DropdownOptionsList(*list(test.columns)),
                    value=None,
                    clearable=False
                )
            ],
            className="mr-3",
        ),
        dbc.FormGroup(
            [
                drc.NamedDropdown(
                    name='C',
                    id='dropdown-layout-3',
                    options=drc.DropdownOptionsList(*list(test.columns)),
                    value=None,
                    clearable=False
                )
            ],
            className="mr-3",
        ),
        dbc.FormGroup(
            [
                drc.NamedDropdown(
                    name='D',
                    id='dropdown-layout-4',
                    options=drc.DropdownOptionsList(*list(test.columns)),
                    value=None,
                    clearable=False
                )
            ],
            className="mr-3",
        ),
        dbc.FormGroup(
            [
                drc.NamedDropdown(
                    name='E',
                    id='dropdown-layout-5',
                    options=drc.DropdownOptionsList(*list(test.columns)),
                    value=None,
                    clearable=False
                )
            ],
            className="mr-3",
        ),
        dbc.Button("Submit", id="Submit",color="primary"),
    ],
    inline=True,
)
@app.callback(Output('form', 'children'),
               [Input('Submit', 'n_clicks'),],
               [State('dropdown-layout-1', 'value'),State('dropdown-layout-2', 'value'),State('dropdown-layout-3', 'value'),
                State('dropdown-layout-4', 'value'),State('dropdown-layout-5', 'value'),])
def update_output_1(submit, values1,values2,values3,values4,values5):
    if (values1 is not None) and (values2 is not None) and (values3 is not None) and (values4 is not None) and (values5 is not None):
        ren={values1:"A",
             values2:"B",
             values3:"C",
             values4:"D",
             values5:"E"
            }
        test.rename(columns=ren, inplace=True)
        print(test)
    return form
        
flag=1
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server()


# In[ ]:




