import plotly.express as px # type: ignore
import streamlit as st

def create_age_distribution(data) -> None:
    fig = px.histogram(
        data,
        x='age',
        color='heart_disease',
        nbins=20,
        title='Distribuição de Idade',
        labels={'age': 'Idade', 'heart_disease': 'Doença Cardíaca'},
        barmode='overlay'
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True)

def create_gender_pie(data) -> None:
    fig = px.pie(
        data,
        names='sexo',
        title='Distribuição por Sexo'
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True)

def create_scatter_plot(data) -> None:
    fig = px.scatter(
        data,
        x='cholesterol',
        y='resting_blood_pressure',
        color='heart_disease',
        trendline="lowess",
        title='Colesterol vs Pressão Arterial',
        labels={
            'cholesterol': 'Colesterol (mg/dL)',
            'resting_blood_pressure': 'Pressão Arterial (mmHg)'
        }
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True)

def create_correlation_heatmap(data) -> None:
    numeric_cols = data.select_dtypes(include=['number']).columns
    corr = data[numeric_cols].corr()
    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        title='Correlação entre Variáveis'
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True)

def create_boxplot(data) -> None:
    fig = px.box(
        data,
        x='tipo_dor_peito',
        y='max_heart_rate',
        color='heart_disease',
        title='Frequência Cardíaca por Tipo de Dor',
        labels={
            'max_heart_rate': 'Frequência Cardíaca Máxima',
            'tipo_dor_peito': 'Tipo de Dor'
        }
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True)

def create_grouped_bar(data) -> None:
    fig = px.bar(
        data.groupby(['sexo', 'heart_disease']).size().reset_index(name='count'),
        x='sexo',
        y='count',
        color='heart_disease',
        barmode='group',
        title='Prevalência por Sexo',
        labels={'count': 'Número de Pacientes', 'sexo': 'Sexo'}
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True)
