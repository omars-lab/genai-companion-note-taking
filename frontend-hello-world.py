import streamlit as st
import datetime
import pandas as pd
import numpy as np
import time

st.title("Title")

with st.sidebar:
    st.header("Side Bar")
    option = st.selectbox("Sidebar Options", ("1st", "2nd", "3rd"))

col1, col2, col3 = st.columns(3)
with col1:
    st.header("First Option: Input Mechanisms")
    if option == "1st":
        st.markdown(f"*This option was selected*")
    # ------------------------------------------
    selections = st.multiselect(
        "Multiselect", [1, 2, 3, 4, 5, 6], [1, 2]
    )
    # ------------------------------------------
    x = st.slider("Choose an x value", 1, 100)
    # ------------------------------------------
    color = st.color_picker("Pick A Color", "#00f900")
    st.write("The current color is", color)
    # ------------------------------------------
    options = ["North", "East", "South", "West"]
    selection = st.pills("Directions", options, selection_mode="multi")
    st.markdown(f"Your selected options: {selection}.")
    # ------------------------------------------
    d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
    st.write("Your birthday is:", d)
    # ------------------------------------------
    t = st.time_input("Set an alarm for", datetime.time(8, 45))
    st.write("Alarm is set for", t)
    # ------------------------------------------
    genre = st.radio(
        "What's your favorite movie genre",
        [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
        index=None,
    )
    st.write("You selected:", genre)
    # ---------------
    on = st.toggle("Activate feature")
    if on:
        st.write("Feature activated!")
    # ------------------------------------------
    option_map = {
        0: ":material/add:",
        1: ":material/zoom_in:",
        2: ":material/zoom_out:",
        3: ":material/zoom_out_map:",
    }
    selection = st.segmented_control(
        "Tool",
        options=option_map.keys(),
        format_func=lambda option: option_map[option],
        selection_mode="single",
    )
    st.write(
        "Your selected option: "
        f"{None if selection is None else option_map[selection]}"
    )
    # ------------------------------------------
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars")
    if selected is not None:
        st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
    # ------------------------------------------
    sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
    selected = st.feedback("thumbs")
    if selected is not None:
        st.markdown(f"You selected: {sentiment_mapping[selected]}")
    # ------------------------------------------
    @st.dialog("Cast your vote")
    def vote(item):
        st.write(f"Why is {item} your favorite?")
        reason = st.text_input("Because...")
        if st.button("Submit"):
            st.session_state.vote = {"item": item, "reason": reason}
            st.rerun()

    if "vote" not in st.session_state:
        st.write("Vote for your favorite")
        if st.button("A"):
            vote("A")
        if st.button("B"):
            vote("B")
    else:
        f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"

with col2:
    st.header("Second Option: Dashboarding & Viz Mechanisms")
    if option == "2nd":
        st.markdown(f"*This option was selected*")
    # ------------------------------------------
    with st.status("Downloading data...", expanded=True) as status:
        st.write("Searching for data...")
        time.sleep(2)
        st.write("Found URL.")
        time.sleep(1)
        st.write("Downloading data...")
        time.sleep(1)
        status.update(
            label="Download complete!", state="complete", expanded=False
        )
    # ------------------------------------------
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    

with col3:
    st.header("Third Option: Documentation Mechanisms")
    if option == "3rd":
        st.markdown(f"*This option was selected*")
    # ------------------------------------------
    st.write("This is :blue[blue], :green[green], :red[red]")
    # ------------------------------------------
    # st.page_link("./frontend.py", label="Main", icon="🏠")
    # st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
    # st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
    # st.page_link("http://www.google.com", label="Google", icon="🌎")
    # ------------------------------------------
    st.info('This is a purely informational message', icon="ℹ️")
    # ------------------------------------------
    with st.spinner("Wait for it...", show_time=True):
        time.sleep(5)
    st.success("Done!")
    # ------------------------------------------
    def get_user_name():
        return 'John'
    with st.echo():
        # Everything inside this block will be both printed to the screen
        # and executed.

        def get_punctuation():
            return '!!!'

        greeting = "Hi there, "
        value = get_user_name()
        punctuation = get_punctuation()

        st.write(greeting, value, punctuation)
    # And now we're back to _not_ printing to the screen
    foo = 'bar'
    st.write('Done!')
    # ---------
    st.json(
        {
            "foo": "bar",
            "stuff": [
                "stuff 1",
                "stuff 2",
                "stuff 3",
            ],
            "level1": {"level2": {"level3": {"a": "b"}}},
        },
        expanded=2,
    )
    # ---------
    st.caption("This is a string that explains something above.")
    st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")
    # ---------
    code = '''def hello():
        print("Hello, Streamlit!")'''
    st.code(code, language="python")
    # ---------
    st.divider()


# DATA VIZ
st.header("Data Visualiation")
df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)  # Same as st.write(df)
# ------------------------------------------
data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
        "progress": [200, 550, 1000, 80],
        "other": ["a", "b", "c", "d"]
    }
)
data_df["revenue"] = data_df["sales"]
data_df["profit"] = data_df["sales"]
st.data_editor(
    data_df,
    column_config={
        "other": "Name",
        "sales": st.column_config.LineChartColumn(
            "Sales (last 6 months)",
            width="medium",
            help="The sales volume in the last 6 months",
            y_min=0,
            y_max=100,
        ),
        "revenue": st.column_config.AreaChartColumn(
            "revenue (last 6 months)",
            width="medium",
            help="The sales volume in the last 6 months",
            y_min=0,
            y_max=100,
        ),
        "profit": st.column_config.BarChartColumn(
            "profit (last 6 months)",
            help="The sales volume in the last 6 months",
            y_min=0,
            y_max=100,
        ),
        "progress": st.column_config.ProgressColumn(
            "Sales volume",
            help="The sales volume in USD",
            format="$%f",
            min_value=0,
            max_value=1000,
        ),
    },
    hide_index=True,
    disabled=True # Don't allow editing of data.
)
# ---------------
# Chart Data
chart_data = pd.DataFrame(np.random.randn(20,3), columns=["a", "b", "c"])
st.area_chart(chart_data)
# ---------------


# CHATBOT MECHANICS
st.header("Chatbot Mechanisms")
# ---------
def stream_data():
    LOREM_IPSUM = "abc "* 100
    for word in LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)
if st.button("Stream data"):
    st.write_stream(stream_data)
# ---------
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
# ---------
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
# ---------


st.button("Rerun")