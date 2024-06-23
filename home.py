import streamlit as st
from streamlit_option_menu import option_menu


def main():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

  # Sidebar navigation
  with st.sidebar:
      selected = option_menu(
          menu_title="Navigation",
          options=["Home", "CAD-Eng ️"],
          icons=["house", "tools"],
          menu_icon="cast",
          default_index=1,
      )

  # Redirect to Home page (assuming it's an external URL)
  if selected == "Home":
      st.markdown("""
          <meta http-equiv="refresh" content="0; url='https://landing-page-url.com'" />
      """, unsafe_allow_html=True)

  left_column, right_column = st.columns(2)

  st.markdown(
      """
      <style>
      @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

      html, body, [class*="css"] {
          font-family: 'Roboto', sans-serif;
      }

      .main-title {
          font-size: 2.5em;
          font-weight: bold;
      }

      .sub-title {
          font-size: 1.5em;
          font-weight: normal;
      }

      .description {
          font-size: 16px;
          font-weight: normal;
      }
      </style>
      """,
      unsafe_allow_html=True,
  )

  # Main content
  st.markdown("<div class='container'>", unsafe_allow_html=True)
  st.markdown("<div class='text-container'>", unsafe_allow_html=True)

  with left_column:
      # Title and subtitle
      st.markdown("   ")
      st.markdown("   ")
      st.markdown("<div class='main-title'>Meet CAD-Eng</div>", unsafe_allow_html=True)
      st.markdown("   ")
      st.markdown("   ")
      st.markdown("<div class='sub-title'>English to CAD. If you think of something that can be built, we will 3D print it!</div>", unsafe_allow_html=True)
      st.markdown("   ")
      st.markdown("   ")
      st.markdown("   ")

      # Description
      st.markdown("<div class='description'>Use our AI chatbot, Oski, to explain what you need. We will show you a preview before we print it.</div>", unsafe_allow_html=True)
      st.markdown("   ")
      st.markdown("   ")
      st.markdown("   ")
      st.markdown("   ")

      # Get started button
      if st.button("GET STARTED", key='get_started', help='Click to get started'):
          st.write("Thank you for clicking the Get Started button!")

  # Removed the closing div for the left column (</div>)

  with right_column:
      # Image container
      st.markdown("<div class='image-container'>", unsafe_allow_html=True)
      st.image("imagehome.png", caption="App and laptop display")  # Update the image path if necessary
      st.markdown("</div>", unsafe_allow_html=True)  #

if __name__ == "__main__":
    main()
