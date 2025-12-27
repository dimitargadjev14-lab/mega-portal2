import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Заглавие и описание
# ---------------------------
st.title("Голям Python Уеб Проект")
st.write("Това е примерен голям проект с Python и Streamlit.")
st.write("Има интерактивни елементи, таблици и графики.")

# ---------------------------
# Странично меню
# ---------------------------
menu = ["Начало", "Калкулатор", "Таблица", "Графики"]
choice = st.sidebar.selectbox("Меню", menu)

# ---------------------------
# Секция: Начало
# ---------------------------
if choice == "Начало":
    st.header("Добре дошъл!")
    name = st.text_input("Как се казваш?")
    if name:
        st.write(f"Здравей, {name}! Радвам се да те видя тук.")
    st.write("Използвай менюто в ляво за да изследваш различни секции.")

# ---------------------------
# Секция: Калкулатор
# ---------------------------
elif choice == "Калкулатор":
    st.header("Калкулатор")
    num1 = st.number_input("Въведи първо число", value=0)
    num2 = st.number_input("Въведи второ число", value=0)
    operation = st.selectbox("Избери операция", ["Събиране", "Изваждане", "Умножение", "Деление"])

    if st.button("Изчисли"):
        if operation == "Събиране":
            result = num1 + num2
        elif operation == "Изваждане":
            result = num1 - num2
        elif operation == "Умножение":
            result = num1 * num2
        elif operation == "Деление":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Грешка: Деление на 0!"
        st.success(f"Резултат: {result}")

# ---------------------------
# Секция: Таблица
# ---------------------------
elif choice == "Таблица":
    st.header("Примерна таблица")
    data = {
        "Име": ["Митко", "Иван", "Мария", "Светлана"],
        "Възраст": [14, 15, 14, 16],
        "Клас": [8, 9, 8, 10]
    }
    df = pd.DataFrame(data)
    st.table(df)

# ---------------------------
# Секция: Графики
# ---------------------------
elif choice == "Графики":
    st.header("Примерна графика")
    # Примерни данни
    fruits = ["Ябълки", "Банани", "Портокали", "Круши"]
    quantity = [10, 15, 7, 12]

    fig, ax = plt.subplots()
    ax.bar(fruits, quantity, color='skyblue')
    ax.set_ylabel("Количество")
    ax.set_title("Брой плодове")
    st.pyplot(fig)

    st.write("Можеш да променяш данните в кода за да виждаш различни графики.")
