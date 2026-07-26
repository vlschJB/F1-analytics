import streamlit as st
import clickhouse_connect
import os

st.set_page_config(page_title="F1 Analytics", layout="wide")

st.title("F1 Analytics Pipeline")
st.markdown("Пет-проект для анализа данных Формулы-1")

try:
    client = clickhouse_connect.get_client(
        host=os.environ.get("CLICKHOUSE_HOST", "clickhouse"),
        port=int(os.environ.get("CLICKHOUSE_PORT", 8123)),
        database=os.environ.get("CLICKHOUSE_DB", "f1db"),
        username=os.environ.get("CLICKHOUSE_USER", "default"),
        password=os.environ.get("CLICKHOUSE_PASSWORD", ""),
    )
    st.success("Подключение к ClickHouse установлено")
except Exception as e:
    st.warning(f"ClickHouse недоступен: {e}")

st.markdown("---")
st.markdown("В разработке: телеметрия, сравнение кругов, live timing")