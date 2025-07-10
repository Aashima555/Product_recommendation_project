```python
import streamlit as st
import pandas as pd

df = pd.read_csv("user_recommendations.csv")

st.set_page_config(page_title="Product Recommender", page_icon="🛍️")

st.title("🛍️ Product Recommendation Engine")
st.markdown("Get personalized product recommendations based on your shopping behavior.")


segment = st.selectbox("Choose your user segment:", df['user_segment'].unique())


filtered_df = df[df['user_segment'] == segment]


user = st.selectbox("Choose a user:", filtered_df['customer_unique_id'])


user_data = filtered_df[filtered_df['customer_unique_id'] == user]

if not user_data.empty:
    st.markdown(f"**Segment:** {user_data['user_segment'].values[0]}")
    st.markdown(f"**Top Category:** {user_data['top_category'].values[0]}")
    st.markdown("### 🛒 Recommended Products:")
    for product in eval(user_data['recommended_products'].values[0]):
        st.markdown(f"- {product}")
else:
    st.warning("No recommendations found for this user.")
