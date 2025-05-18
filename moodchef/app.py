import streamlit as st
from models import User, RecommendationEngine
from data import get_sample_meals
from auth import login, load_db, save_db
from payment import simulate_payment

st.set_page_config(page_title="MoodChef", page_icon="🍽️")
st.title("🍽️ MoodChef - AI Mood-based Meal Recommender")

username = st.text_input("👤 Enter your username to continue")

if username:
    user_data = login(username)
    user = User(username)

    st.sidebar.header("Your Mood")
    mood = st.sidebar.selectbox("How are you feeling?", ["happy", "sad", "angry","lazy"])
    diet = st.sidebar.selectbox("Diet Preference", ["Any", "veg", "non-veg"])

    if st.sidebar.button("🎯 Recommend Meal"):
        user.update_mood(mood)
        engine = RecommendationEngine(get_sample_meals())
        meals = engine.recommend(mood, None if diet == "Any" else diet)

        st.subheader(f"Recommended meals for mood: *{mood}*")
        for m in meals:
            st.markdown(f"🍴 **{m.name}** --*({m.type})*")
            st.markdown(f"🧂 Ingredients: `{', '.join(m.ingredients)}`")
            st.markdown("---")

    st.subheader("💳 Upgrade to Premium")
    if st.button("Pay $5 for 1-week plan"):
        payment = simulate_payment(username)
        st.success("Payment Successful!")
        st.json(payment)

    # Show mood history
    db = load_db()
    history = db[username].get("mood_history", [])
    history.append(mood)
    db[username]["mood_history"] = history
    save_db(db)

    with st.expander("🕘 Mood History"):
        st.write(history)
                                                    