import qcedu as edu
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_bio as dashbio
import json
import six.moves.urllib.request as urlreq
from six import PY3

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True
app.config.suppress_callback_exceptions = True # needed for simple multi-page apps, see https://dash.plot.ly/urls

model_data = urlreq.urlopen(
    'https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/' +
    'mol3d/model_data.js'
).read()
styles_data = urlreq.urlopen(
    'https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/' +
    'mol3d/styles_data.js'
).read()

if PY3:
    model_data = model_data.decode('utf-8')
    styles_data = styles_data.decode('utf-8')

model_data = json.loads(model_data)
styles_data = json.loads(styles_data)



app.layout = html.Div([
	html.Div([
		dbc.Navbar(
	    [
	        html.A(
	            # Use row and col to control vertical alignment of logo / brand
	            dbc.Row(
	                [
	                    dbc.Col(html.Img(src='/assets/images/logo.svg', height="30px")),
	                ],
	                align="center",
	                no_gutters=True,
	            ),
	        ),

	  #      dbc.Nav(
			#     [
			#        	dbc.NavItem(dbc.NavLink("ABOUT", active=True, href="#"), className='d-md-down-none'),
		 #        	dbc.NavItem(dbc.NavLink("GET STARTED", active=True, href="#"), className='d-md-down-none'),
		 #        	dbc.NavItem(dbc.NavLink("BLOG", active=True, href="#"), className='d-md-down-none'),
			#         dbc.DropdownMenu(
			#             children=[
			#                 dbc.DropdownMenuItem("Page 1", header=True),
			#                 dbc.DropdownMenuItem("Page 2", href="#"),
			#                 dbc.DropdownMenuItem("Page 3", href="#"),
			#             ],
			#             nav=True,
			#             in_navbar=True,
			#             color='link',
			#             label="ECOSYSTEM",
		 #        	),
		 #        	dbc.DropdownMenu(
			#             children=[
			#                 dbc.DropdownMenuItem("Page 1", header=True),
			#                 dbc.DropdownMenuItem("Page 2", href="#"),
			#                 dbc.DropdownMenuItem("Page 3", href="#"),
			#             ],
			#             nav=True,
			#             in_navbar=True,
			#             label="DOCUMENTATION",
		 #        	),
		 #        	dbc.DropdownMenu(
			#             children=[
			#                 dbc.DropdownMenuItem("Page 1", header=True),
			#                 dbc.DropdownMenuItem("Page 2", href="#"),
			#                 dbc.DropdownMenuItem("Page 3", href="#"),
			#             ],
			#             nav=True,
			#             in_navbar=True,
			#             label="GITHUB",
		 #        	),
		 #        	dbc.DropdownMenu(
			#             children=[
			#                 dbc.DropdownMenuItem("Page 1", header=True),
			#                 dbc.DropdownMenuItem("Page 2", href="#"),
			#                 dbc.DropdownMenuItem("Page 3", href="#"),
			#             ],
			#             nav=True,
			#             in_navbar=True,
			#             color='success',
			#             label="Apps",
		 #        	),
			#     ],
			#     navbar=True,
			#     className='ml-auto',
			#     style={'font-size': '15px'}
			# )
	    ],
	    color="white",
	    light=True,
		),
	], className='container-fluid ml-0 mr-0 pl-5 pr-5', style={'background-color': 'white'}),
	html.Div([
		html.Div([
			# dbc.Row([
			# 	dbc.Col(
			# 		dbc.Input(id="input", placeholder="Explore molecules", type="text", style={'height': '60px', 'font-size': '20px'}),
			# 		width={"size": 6, "offset": 3},
			# 		),
			# ], className='align-items-center', style={'padding-top': '150px'}),
			dbc.Row([
				dbc.Col([
						dbc.Input(id="text_ide", placeholder="Explore molecules", type="text", list="molecular", style={'height': '60px', 'font-size': '20px'}),						
						# edu.datalist(id="molecular"),
					
						html.Table([
							html.Td(edu.datalist(id="molecular"))
						], style={'table-layout': 'fixed', 'WORD-BREAK': 'break-all'})
					], width=5),
			], className='align-items-center', style={'padding-top': '70px'},  justify="center"),
			dbc.Row([
				dbc.Col(
					html.P(html.H2("Search by common name, scienfic name, or formula"), className='text-secondary text-center'),
				),
			], className='align-items-center', style={'padding-top': '5px'})
		], className='container')
	], style={'background-image': 'url("https://mdbootstrap.com/img/Photos/Others/images/91.jpg")', 'height': '200px'}),

	html.Div([
		dbc.Row([
			dbc.Col(
				edu.eduside(),
								       
				width={"size": 3},
				style={'background-color':'white'},
				className='pl-0 pr-0',
				),
			dbc.Col(
				html.Div([
				    dashbio.Molecule3dViewer(
				        id='my-dashbio-molecule3d',
				        styles=styles_data,
				        modelData=model_data
				    ),
				    html.Hr(),
				    html.Div(id='molecule3d-output')
				]),
				width={"size": 6},
				className='pl-0 pr-0'
			),
			dbc.Col(
				dbc.ListGroup(
				    [
				        dbc.ListGroupItem(
				            [
				                dbc.ListGroupItemHeading([
				                	html.P(html.H1("Information"), className='text-center')
				                	
				                ]),
				            ]
				        ),
				        dbc.ListGroupItem(
				            [
				                dbc.Row([
				                	dbc.Col(dbc.ListGroupItemText([
				                		html.P(html.H4("Molecular Formula:"), className='text-center')
				                	]),
				                		width={"size": 5},
				                	),
				                	dbc.Col(dbc.ListGroupItemText([
				                		html.P("H20", id="data1", className='text-center', style={'font-size': '12px'})
				                	]),
				                		width={"size": 7},
				                	),

				                ])
				            ]
				        ),
				        dbc.ListGroupItem(
				            [
				                dbc.Row([
				                	dbc.Col(dbc.ListGroupItemText([
				                		html.Br(),
				                		html.Br(),
				                		html.P(html.H4("Chemical Names:"), className='text-center'),
				                	]),
				                		width={"size": 5},
				                	),
				                	dbc.Col(dbc.ListGroupItemText([
				                		html.P("water", className='text-center', style={'font-size': '12px'}),
				                		html.P("dihydrgen oxide", className='text-center', style={'font-size': '12px'}),
				                		html.P("purfied water", className='text-center', style={'font-size': '12px'}),
				                	]),
				                		width={"size": 7},
				                	),

				                ])
				            ]
				        ),
				        dbc.ListGroupItem(
				            [
				                dbc.Row([
				                	dbc.Col(dbc.ListGroupItemText([
				                		html.P(html.H4("Molecular Weight:"), className='text-center')
				                	]),
				                		width={"size": 5},
				                	),
				                	dbc.Col(dbc.ListGroupItemText([
				                		html.P("18.05 g/mol", className='text-center', style={'font-size': '12px'})
				                	]),
				                		width={"size": 7},
				                	),

				                ])
				            ]
				        ),
				        dbc.ListGroupItem(
				            [
				                dbc.Row([
				                	dbc.Col(dbc.ListGroupItemText([
				                		html.P(html.H4("PubChem CID (?):"), className='text-center')
				                	]),
				                		width={"size": 5},
				                	),
				                	dbc.Col(dbc.ListGroupItemText([
				                		html.P("962", className='text-center', style={'font-size': '12px'})
				                	]),
				                		width={"size": 7},
				                	),

				                ])
				            ]
				        ),
				        dbc.ListGroupItem(
				            [
				                dbc.Row([
				                	dbc.Col(dbc.ListGroupItemText([
				                		html.Br(),
				                		html.Br(),
				                		html.Br(),
				                		html.P(html.H4("Physical Properties:"), className='text-center')
				                	]),
				                		width={"size": 5},
				                	),
				                	dbc.Col(dbc.ListGroupItemText([
				                		html.P("clear", className='text-center', style={'font-size': '12px'}),
				                		html.P("colorless", className='text-center', style={'font-size': '12px'}),
				                		html.P("odorless", className='text-center', style={'font-size': '12px'}),
				                		html.P("tasteless", className='text-center', style={'font-size': '12px'}),
				                		html.P("freezes below 0 ℃", className='text-center', style={'font-size': '12px'}),
				                		html.P("boils above 100 ℃", className='text-center', style={'font-size': '12px'}),
				                	]),
				                		width={"size": 7},
				                	),

				                ])
				            ]
				        ),
				        dbc.ListGroupItem(
				            [
				                dbc.Row([
				                	dbc.Col(dbc.ListGroupItemText([
				                		html.Br(),
				                		html.P(html.H4("Chemical Safety:"), className='text-center')
				                	]),
				                		width={"size": 5},
				                	),
				                	dbc.Col(dbc.ListGroupItemText([
				                		html.P((html.A(html.H4("Laboratory"), href='#')), className='text-center'),
				                		html.P((html.A(html.H4("Safety Summary"), href='#')), className='text-center'),
				                		html.P((html.A(html.H4("(LCSS) Datasheet"), href='#')), className='text-center'),
				                	]),
				                		width={"size": 7},
				                	),

				                ])
				            ]
				        ),
				    ]),
				width={"size": 3},
				style={'background-color':'white'},
				className='pl-0 pr-0'
				),
		]),
	], className='container-fluid')


   ])

@app.callback(
    Output(component_id='data1', component_property='children'),
    [Input(component_id='text_ide', component_property='value')]
)
def update_right_table(input_value):
	if input_value is None:
		return "H2O"
	else:
		return input_value


if __name__ == '__main__':
    app.run_server(debug=True)
