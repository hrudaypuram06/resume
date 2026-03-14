import plotly.graph_objects as go

def skill_chart(skills):

    categories = ["Python","ML","Web","Database","Visualization"]

    values = [0,0,0,0,0]

    for s in skills:

        if s in ["python"]:
            values[0]+=1

        if s in ["machine learning","deep learning"]:
            values[1]+=1

        if s in ["html","css","javascript","react"]:
            values[2]+=1

        if s in ["sql"]:
            values[3]+=1

        if s in ["tableau","power bi"]:
            values[4]+=1

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself'
    ))

    return fig
