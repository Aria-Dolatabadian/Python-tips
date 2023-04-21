import plotly.express as px
data=[[500, 450, 460, 470, 580], [450, 430, 410, 350, 150], [400, 390, 380, 150, 50]]
fig = px.imshow(data,
                labels=dict(x="Cultivar", y="Stress intensity", color="Yield"),
                x=['Westar', 'Hyola', 'Glacier', 'Quinta', 'Tina'],
                y=['No Stress', 'Mild Stress', 'Severe Stress']
               )
fig.update_xaxes(side="top")
fig.show()
