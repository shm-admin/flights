import streamlit as st
import random
import smtplib
from email.mime.text import MIMEText # Module-email 
from email.mime.multipart import MIMEMultipart # Module-multipart
import mysql.connector as m
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="SHM Airlines",
    page_icon="✈️", 
    layout="centered",)

st.markdown("#### 🚫 Do not refresh the page 🚫")
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background-image: url("https://wallpapercave.com/wp/wp10724311.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.2); /
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state variables
if "page" not in st.session_state:
    st.session_state.page = "main"
if "email" not in st.session_state:
    st.session_state.email = None
if "username" not in st.session_state:
    st.session_state.username = None
if "mode" not in st.session_state:
    st.session_state.mode = "Login"
if "selected_option" not in st.session_state:
    st.session_state.selected_option = None

# Home Page Sidebar
def sidebar():
    st.sidebar.title("Navigation")
    st.sidebar.button("👤 Your Account", on_click=lambda: st.session_state.update(page="Account"))
    st.sidebar.button("✈️ Book Ticket", on_click=lambda: st.session_state.update(page="Book Ticket"))
    st.sidebar.button("✏️ Update Ticket", on_click=lambda: st.session_state.update(page="Update Ticket"))
    st.sidebar.button("❌ Cancel Ticket", on_click=lambda: st.session_state.update(page="Cancel Ticket"))
    st.sidebar.button("📅 Your Bookings", on_click=lambda: st.session_state.update(page="Your Bookings"))
    st.sidebar.button("📋 Rules and Regulations", on_click=lambda: st.session_state.update(page="Rules"))
    st.sidebar.button("📝 Feedback and Queries", on_click=lambda: st.session_state.update(page="Feedback and Queries"))
    st.sidebar.button("🛈  About Our Airline", on_click=lambda: st.session_state.update(page="About"))
    if st.sidebar.button("🚪 Logout"):
        # Clear session state and reset all session variables
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.session_state.page = "main"  # Redirect to the main page
        st.success("You have logged out successfully.")

# Admin Page Sidebar
def admin_sidebar():
    st.sidebar.title("Navigation")
    st.sidebar.button("👤 Passenger Details", on_click=lambda: st.session_state.update(page="t_details"))
    st.sidebar.button("✈️ Flight Details", on_click=lambda: st.session_state.update(page="f_details"))
    st.sidebar.button("👥 User Details", on_click=lambda: st.session_state.update(page="u_details"))
    st.sidebar.button("💬 Feedback and Queries", on_click=lambda: st.session_state.update(page="fq_details"))
    st.sidebar.button("✉️ Send Reply", on_click=lambda: st.session_state.update(page="reply"))
    if st.sidebar.button("🚪 Logout"):
        # Clear session state and reset all session variables
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.session_state.page = "main" 
        st.success("You have logged out successfully.")

# Function to connect to MySQL database
def connect_to_db():
    mycon = m.connect(host="192.168.1.4:8501",user="root",password="mithu",database="airlines")
    return mycon

# Function to generate an OTP
def generate_otp():
    return random.randint(100000, 999999)

# Function to send OTP via email
def send_otp_email(recipient_email):
    otp = random.randint(100000, 999999)
    st.session_state.otp = otp  # Save OTP in session state
    try:
        sender_email = "shm.airlines2024@gmail.com"
        sender_password = "ispa gtza rkin drcy"
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        subject = "OTP for Verification"
        message = f"Your OTP is: {otp}. This OTP is valid for 5 minutes."
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        st.success(f"OTP sent to {recipient_email}")
    except smtplib.SMTPConnectError:
        st.error("Failed to connect to the SMTP server. Check your internet connection.")
    except smtplib.SMTPAuthenticationError:
        st.error("Authentication failed. Check your email or password.")
    except smtplib.SMTPRecipientsRefused:
        st.error(f"Email address '{recipient_email}' is invalid.")
    except smtplib.SMTPException as e:
        st.error(f"An SMTP error occurred: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
    
def send_ticket_email(to_email, flight_details, passenger_details):
    sender_email = "shm.airlines2024@gmail.com"
    sender_password = "ispa gtza rkin drcy"

    subject = "Your Flight Ticket Confirmation"

    # Format the ticket as plain text with loops for passenger details
    ticket_content = f"""
    ============================
    Flight Ticket Confirmation
    ============================

    Flight Details:
    ----------------
    Flight Number: {flight_details['fid']}
    Departure: {flight_details['departure']} -> {flight_details['arrival']}
    Date of Travel: {flight_details['date']}
    Time of Departure: {flight_details['dtime']}
    Class: {flight_details['class']}
    Total Price: ₹{flight_details['total_price']}

    ---------------------------
    Passenger Information:
    ---------------------------"""

    # Add passenger details dynamically using a for loop
    for idx, passenger in enumerate(passenger_details, 1):
        ticket_content += f"""
        Passenger {idx}:
        -----------------
        Passenegr ID: {passenger['id']}
        Name: {passenger['name']}
        Age: {passenger['age']}
        Gender: {passenger['gender']}
        Food Preference: {passenger['inflight_food']}
        """

    ticket_content += """
    ============================
    Thank you for choosing our airline!
    ============================
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(ticket_content, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
            print(f"Tickets have been sent to {to_email}")
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

def calculate_ticket_price(base_price, class_multiplier, num_passengers):
    return base_price * class_multiplier * num_passengers

def cities():
    my_db = connect_to_db()
    cursor = my_db.cursor()
    query1 = "SELECT DISTINCT departure FROM flights;"
    query2 = "SELECT DISTINCT arrival FROM flights;"
    cursor.execute(query1)
    dept = [item[0] for item in cursor.fetchall()]
    cursor.execute(query2)
    arr = [item[0] for item in cursor.fetchall()]
    my_db.close()
    return dept, arr

def search_flights(d_city, a_city):
    my_db = connect_to_db()
    cursor = my_db.cursor()
    query = "SELECT * FROM flights WHERE departure = %s AND arrival = %s;"
    cursor.execute(query, (d_city, a_city))
    details = cursor.fetchall()
    my_db.close()
    return details

def generate_pid():
    return random.randint(1, 10000)

def insert_data(data):
    if not data:
        print("No data to insert.")
        return
    columns = ", ".join(data[0].keys())  
    placeholders = ", ".join(["%s"] * len(data[0]))  
    query = f"INSERT INTO passenger_details ({columns}) VALUES ({placeholders})"
    my_db = connect_to_db()
    cursor = my_db.cursor()
    try:
        values = [tuple(d.values()) for d in data]
        cursor.executemany(query, values)
        my_db.commit()
    except m.Error as e:
        print(f"Error: {e}")
        my_db.rollback()
    finally:
        cursor.close()
        my_db.close()

def fetch_passenger_data():
    db_connection = connect_to_db()
    cursor = db_connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query,(st.session_state.email,))
    record = cursor.fetchone()
    db_connection.close()
    return record

def fetch_passenger_details2():
    db_connection = connect_to_db()
    cursor = db_connection.cursor(dictionary=True)
    query = "SELECT * FROM passenger_details WHERE email = %s;"
    cursor.execute(query,(st.session_state.email,))
    data = cursor.fetchall()
    db_connection.close()
    return data

def check_user_login(email, password):
    db_connection = connect_to_db()
    if db_connection:
        cursor = db_connection.cursor()
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        result = cursor.fetchone()
        if result:
            username = result[2]
            st.session_state.username = username
            return result
        db_connection.close()        
    return None

def check_user_signin(email):
    db_connection = connect_to_db()
    if db_connection:
        cursor = db_connection.cursor()
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        if result:
            username = result[2]
            st.session_state.username = username
            return result
        db_connection.close()
    return None

def save_user(email, password, username):
    db_connection = connect_to_db()
    if db_connection:
        cursor = db_connection.cursor()
        query = "INSERT INTO users (email, password, username) VALUES (%s, %s, %s)"
        cursor.execute(query, (email, password, username))
        db_connection.commit()
        db_connection.close()
        st.success("User  registered successfully!")
    else:
        st.error("Failed to register user.")

def fetch_passenger_data1(passenger_id, flight_number):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM passenger_details WHERE id = %s AND fid = %s AND email = %s"
        cursor.execute(query, (passenger_id, flight_number,st.session_state.email))
        result = cursor.fetchall()
        connection.close()
        return result
    return []

def update_passenger_data(passenger_id, flight_number, name, gender, age, inflight_food):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
            UPDATE passenger_details
            SET name = %s, gender = %s, age = %s, inflight_food = %s
            WHERE id = %s AND fid = %s
            """
            cursor.execute(query, (name, gender, age, inflight_food, passenger_id, flight_number))
            connection.commit()
            st.success("Passenger data updated successfully!")
        except m.Error as err:
            st.error(f"Error updating data: {err}")
        finally:
            cursor.close()
            connection.close()
            
def display_updated_passenger_data(passenger_id, flight_number):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
            SELECT * FROM passenger_details
            WHERE id = %s AND fid = %s
            """
            cursor.execute(query, (passenger_id, flight_number))
            result = cursor.fetchall()
            return result
        except m.Error as err:
            st.error(f"Error fetching updated data: {err}")
        finally:
            cursor.close()
            connection.close()
    return []

def search_records(search_type, search_value):
    db_connection = connect_to_db()
    if db_connection:
        cursor = db_connection.cursor(dictionary=True)
        if search_type == "Passenger ID":
            query = "SELECT * FROM passenger_details WHERE id = %s"
            cursor.execute(query, (search_value,))
        elif search_type == "Name":
            query = "SELECT * FROM passenger_details WHERE name = %s"
            cursor.execute(query, (search_value,))
        elif search_type == "Date":
            query = "SELECT * FROM passenger_details WHERE flight_date = %s"
            cursor.execute(query, (search_value,))
        else:
            st.error("Invalid search type.")
            db_connection.close()
            return []
        records = cursor.fetchall()
        db_connection.close()
        return records
    else:
        return []

def search_records(search_value):
    db_connection = connect_to_db()
    if db_connection:
        cursor = db_connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (search_value,))
        records = cursor.fetchall()
        db_connection.close()
        return records
    else:
        return []

def search_records(search_value1, search_value2):
    db_connection = connect_to_db()
    if db_connection:
        cursor = db_connection.cursor(dictionary=True)
        if search_type == "Departure & Arrival":
            query = "SELECT * FROM flights WHERE departure = %s and arrival = %s"
            cursor.execute(query, (search_value1,search_value2))
        records = cursor.fetchall()
        db_connection.close()
        return records
    else:
        return []

def send_reply_email(reply_email, subject, message):
    try:
        sender_email = "shm.airlines2024@gmail.com"
        sender_password = "ispa gtza rkin drcy"
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Construct the email
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = reply_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        return True
    except Exception as e:
        st.error(f"Failed to send email: {e}")
        return False

# Main Page
if "page" not in st.session_state:
    st.session_state.page = "main"

if st.session_state.page == "main":
    st.title("Welcome to SHM Airlines")
    st.session_state.mode = st.radio("Choose an option:", ["Login", "Sign Up", "Admin"])

    if st.session_state.mode == "Admin":
        admin_password = st.text_input("Enter Admin Password:", type="password")
        if st.button("Login as Admin"):
            if admin_password == "1234":
                st.session_state.page = "admin"
            else:
                st.error("Incorrect password!")

    elif st.session_state.mode == "Sign Up":
        email = st.text_input("Enter your E-Mail:")
        password = st.text_input("Enter your Password:", type="password")
        username = st.text_input("Enter your Name:")
        st.session_state.username = username
        st.subheader("*Terms and Conditions*")
        st.markdown("""
                    Welcome to SHM Airlines
                    By signing in, you agree to comply with the following terms and conditions:

                    1.Account Usage:
                     - The account is for your personal use only. You are responsible for maintaining the confidentiality of your login credentials.
                     - Unauthorized access to or use of your account is strictly prohibited.

                    2.Accuracy of Information:
                     - You agree to provide accurate and up-to-date information during registration and while using our services.
                     - SHM Airlines reserves the right to verify and validate the information provided.

                    3.Flight Bookings and Modifications:
                     - All bookings are subject to availability and governed by our fare rules, cancellation policies, and rebooking terms.
                     - Any changes to bookings must comply with SHM Airlines' modification and refund policies.

                    4.Privacy and Data Collection:
                     - By signing in, you consent to the collection, use, and storage of your personal data in accordance with our Privacy Policy.
                     - SHM Airlines uses your information to improve services, send updates, and process bookings.

                    5.Prohibited Activities:
                     - Use of the platform for fraudulent activities, unauthorized access, or harm to SHM Airlines' systems is strictly prohibited.
                     - Engaging in abusive behavior, harassment, or violations of airline policies may result in account suspension or legal action.

                    6.Liability:
                     - SHM Airlines is not responsible for losses arising from delays, cancellations, or other issues beyond our control (e.g., weather, air traffic control decisions).
                     - Compensation, if applicable, will be in accordance with our Customer Service Agreement.

                    7.Modifications to Terms:
                     - SHM Airlines reserves the right to modify these terms at any time. Continued use of the platform constitutes acceptance of the revised terms.
                    
                    8.Governing Law:
                     - These terms are governed by the laws of the country where SHM Airlines operates. Any disputes will be resolved under the jurisdiction of the respective courts.
                    """)
        check = st.checkbox("I agree to the terms and conditions")
        if check:
            if st.button("Get OTP"):
                if email and password and username:
                    st.session_state.email = email
                    send_otp_email(email)
                    st.session_state.otp_sent = True
                else:
                    st.error("Please fill in all required fields!")

            if st.session_state.get("otp_sent", False):
                st.title("OTP Verification")
                otp_input = st.text_input("Enter the OTP:", type="password")
                verify_button = st.button("Verify OTP")
                resend_otp_button = st.button("Resend OTP")

                if verify_button:
                    if otp_input == str(st.session_state.get("otp", "")):
                        st.success("OTP Verified Successfully!")
                        if st.session_state.mode == "Sign Up":
                            save_user(email, password, username)  # Save user during Sign Up
                        st.session_state.page = "home"
                        st.session_state.otp_sent = False
                    else:
                        st.error("Incorrect OTP. Please try again.")

                if resend_otp_button:
                    send_otp_email(email)
                    st.success("A new OTP has been sent.")
        else:
            st.warning("You must agree to the Terms and Conditions to proceed.")

    elif st.session_state.mode == "Login":
        email = st.text_input("Enter your registered E-Mail:")
        password = st.text_input("Enter your Password:", type="password")
        record = check_user_login(email, password)
        if record:
            if st.button("Get OTP"):
                if email and password and st.session_state.mode == "Login":
                    st.session_state.email = email
                    send_otp_email(email)
                    st.session_state.otp_sent = True
                else:
                    st.error("Please fill in all required fields!")

            if st.session_state.get("otp_sent", False):
                st.title("OTP Verification")
                otp_input = st.text_input("Enter the OTP:", type="password")
                verify_button = st.button("Verify OTP")
                resend_otp_button = st.button("Resend OTP")

                if verify_button:
                    if otp_input == str(st.session_state.get("otp", "")):
                        st.success("OTP Verified Successfully!")
                        st.session_state.page = "home"
                        st.session_state.otp_sent = False
                    else:
                        st.error("Incorrect OTP. Please try again.")

                if resend_otp_button:
                    send_otp_email(email)
                    st.success("A new OTP has been sent.")

# Admin page
elif st.session_state.page == "admin":
    st.title("ADMIN")
    st.write('''Welcome, Admin!
You are logged into the SHM Airlines Admin Dashboard. From here, you can manage various aspects of the airline system efficiently and effectively.''')
    admin_sidebar()

# t_details page
elif st.session_state.page == "t_details":
    admin_sidebar()
    # Streamlit UI for Search
    st.title("Search Passenger Records")
    search_type = st.selectbox("Search By:", ["Passenger ID", "Name", "Date (YYYY-MM-DD)", "Display all passengers"])

    if search_type != "Display all passengers":
        search_value = st.text_input(f"Enter {search_type}:")
        if st.button("Search"):
            if search_value.strip():  # Ensure the input is not empty
                data = search_records(search_type, search_value)
                if data:
                    st.success(f"Found {len(data)} record(s) matching {search_type}: {search_value}")
                    df = pd.DataFrame(data)
                    st.dataframe(df)
                else:
                    st.warning(f"No records found for {search_type}: {search_value}")
            else:
                st.error(f"Please enter a valid {search_type}.")
    
    else:
        db_connection = connect_to_db()
        cursor = db_connection.cursor(dictionary=True)
        query = "SELECT * FROM passenger_details"
        cursor.execute(query)
        records = cursor.fetchall()
        db_connection.close()
        df = pd.DataFrame(records)
        st.dataframe(df)
    
#u_details
elif st.session_state.page == "u_details":
    admin_sidebar()
    st.title("Search User Records")
    search_type = st.selectbox("Search By:", ["Email", "Display all users"])
    if search_type == "Email":
        search_value = st.text_input(f"Enter email id:")
        if st.button("Search"):
            if search_value.strip():  # Ensure the input is not empty
                data = search_records(search_value)
                if data:
                    st.success(f"Found {len(data)} record(s) matching {search_value}")
                    df = pd.DataFrame(data)
                    st.dataframe(df)
                else:
                    st.warning(f"No records found for {search_value}")
            else:
                st.error(f"Please enter a valid {search_type}.")
    else:
        db_connection = connect_to_db()
        cursor = db_connection.cursor(dictionary=True)
        query = "SELECT * FROM users"
        cursor.execute(query)
        records = cursor.fetchall()
        db_connection.close()
        df = pd.DataFrame(records)
        st.dataframe(df)
  
#f_details
elif st.session_state.page == "f_details":
    admin_sidebar()
    # Streamlit UI for Search
    st.title("Search Flights")
    search_type = st.selectbox("Search By:", ["Display all flights", "Departure & Arrival"])
    if search_type == "Departure & Arrival": 
        search_value1 = st.text_input(f"Enter Departure Airport{search_type}:")
        search_value2 = st.text_input(f"Enter Arrival Airport{search_type}:")
        if st.button("Search"):
            if search_value1.strip and search_value2.strip():  # Ensure the input is not empty
                data = search_records(search_value1, search_value2)
                if data:
                    st.success(f"Found {len(data)} record(s) matching {search_type}: {search_value1} & {search_value2}")
                    df = pd.DataFrame(data)
                    st.dataframe(df)
                else:
                    st.warning(f"No records found for {search_type}: {search_value1} & {search_value2}")
            else:
                st.error(f"Please enter a valid {search_type}.")
    
    else:
        db_connection = connect_to_db()
        cursor = db_connection.cursor(dictionary=True)
        query = "SELECT * FROM flights"
        cursor.execute(query)
        records = cursor.fetchall()
        db_connection.close()
        df = pd.DataFrame(records)
        st.dataframe(df)

# fq_details
elif st.session_state.page == "fq_details":
    admin_sidebar()
    db_connection = connect_to_db()
    cursor = db_connection.cursor(dictionary=True)
    query = "SELECT * FROM feedbacks"
    cursor.execute(query)
    records = cursor.fetchall()
    db_connection.close()
    if records:
        df = pd.DataFrame(records)
        st.dataframe(df)
    else:
        st.write('No Feedbacks or Queries.')

# Send reply
elif st.session_state.page == 'reply':
    admin_sidebar()
    # Input fields
    reply_email = st.text_input("Recipient Email:", placeholder="Enter recipient's email")
    subject = st.text_input("Subject:", placeholder="Enter email subject")
    message = st.text_area("Message:", placeholder="Type your reply message here")

    # Button to send email
    if st.button("Send Reply"):
        if reply_email and subject and message.strip():
            if send_reply_email(reply_email, subject, message):
                st.success("Reply sent successfully!")
            else:
                st.error("Failed to send reply. Please check the details and try again.")
        else:
            st.warning("Please fill in all the fields before sending.")

# Home Page
elif st.session_state.page == "home":
    st.title(f"Welcome, {st.session_state.username}!")
    st.write("You have successfully logged in.")
    sidebar()

# Book Ticket Page
elif st.session_state.page == "Book Ticket":
    sidebar()
    st.title("Book Ticket")
    d_cities, a_cities = cities()
    flight_classes = {'Economy': 1.0, 'Business': 2.5, 'First Class': 5.0}
    departure_city = st.selectbox("Select Departure City", d_cities)
    arrival_city = st.selectbox("Select Arrival City", a_cities)

    if departure_city == arrival_city:
        st.error("Departure and arrival cities cannot be the same. Please select different cities.")
    else:
        flight_details = search_flights(departure_city, arrival_city)

        if flight_details:
            st.subheader("Available Flights")
            st_flight_details = pd.DataFrame(flight_details, columns=["Flight No", "Departure", "Arrival", "Flight Time", "Dep. Time", "Base Price"])
            st.dataframe(st_flight_details)

            fnum = st.text_input("Enter your flight number")
            flight_class = st.selectbox("Select Flight Class", list(flight_classes.keys()))
            travel_date = st.date_input("Select date of travel")

            if fnum and travel_date > date.today():
                flight_info = next((f for f in flight_details if f[0] == fnum), None)
                if flight_info:
                    base_price = flight_info[5]
                    departure_time = flight_info[4]
                    total_ftime = flight_info[3]

                    num_passengers = st.number_input("Number of Passengers", min_value=1, value=1)
                    passenger_details = []

                    for i in range(1, num_passengers + 1):
                        st.subheader(f"Passenger {i}")
                        name = st.text_input(f"Enter name for Passenger {i}:", key=f"name_{i}")
                        age = st.number_input(f"Enter age for Passenger {i}:", min_value=1, step=1, key=f"age_{i}")
                        gender = st.radio(f"Choose gender for Passenger {i}:", ["Male", "Female", "Others"], key=f"gender_{i}")
                        food = st.radio(f"Choose food preference for Passenger {i}:", ["Veg", "Non-Veg", "None"], key=f"food_{i}")
                        if name.strip():
                            passenger_id = generate_pid()
                            passenger_details.append({
                                "fid": fnum,
                                "id": passenger_id,
                                "name": name,
                                "email": st.session_state.email,
                                "gender": gender,
                                "age": age,
                                "inflight_food": food,
                                "seat_type": flight_class,
                                "flight_date": travel_date
                            })
                
                    formatted_date = travel_date.strftime('%Y-%m-%d')
                    class_multiplier = flight_classes[flight_class]
                    total_price = calculate_ticket_price(base_price, class_multiplier, num_passengers)
                    flight_info += (formatted_date,flight_class,total_price)
                    flight_infod = {"fid":flight_info[0],"departure":flight_info[1],"arrival":flight_info[2],"date":formatted_date,"dtime":flight_info[4],"class":flight_info[7],"total_price":flight_info[8]}

                    st.subheader(f"Flight Details:")
                    st.write(f"Departure City: {departure_city}")
                    st.write(f"Arrival City: {arrival_city}")
                    st.write(f"Class: {flight_class}")
                    st.write(f"Number of Passengers: {num_passengers}")
                    st.write(f"Base Price: ₹{base_price}")
                    st.write(f"Class Multiplier: {class_multiplier}")
                    st.write(f"Total Price: ₹{total_price:.2f}")

                    if st.button("Confirm Booking"):
                        if len(passenger_details) == num_passengers:
                            insert_data(passenger_details)
                            send_ticket_email(st.session_state.email,flight_infod,passenger_details)
                            st.success(f"Your flight from {departure_city} to {arrival_city} has been successfully booked!")
                        else:
                            st.error("Please fill in all passenger details before confirming.")
                else:
                    st.warning("Invalid flight number.")
            else:
                st.warning("Travel date must be in the future.")
        else:
            st.info("No flights found!")
    
# Cancel Ticket Page
elif st.session_state.page == "Cancel Ticket":
    sidebar()
    st.title("Cancel Ticket")
    current_date = date.today()
    record = fetch_passenger_details2()
    if record:
        present_data,present_pid = [],[]
        for i in record:
            if i["flight_date"] > current_date:
                present_data.append(i)
                present_pid.append(i["id"])
        present_sdata = pd.DataFrame(present_data)
        st.dataframe(present_sdata)
        pid = st.number_input("Enter the passenger ID to be cancelled",min_value=1,step=1)
        if pid in present_pid:
            if st.button("Cancel Ticket"):
                db_connection = connect_to_db()
                cursor = db_connection.cursor(dictionary=True)
                try:
                    query = "DELETE FROM passenger_details WHERE id = %s AND email = %s;"
                    cursor.execute(query,(pid,st.session_state.email))
                    db_connection.commit()
                    db_connection.close()
                    st.success("Ticket Cancelled Successfully")
                except Exception:
                    st.error("Enter the correct ticket details!")
        else:
            st.info("Enter a valid passenger ID")
    else:
        st.info("No ticket found")

# Update Ticket Page
elif st.session_state.page == "Update Ticket":
    sidebar()
    st.title("Update Ticket")
    # Streamlit UI for updating tickets
    st.subheader("Search Passenger Details")
    passenger_id = st.text_input("Enter Passenger ID for Search:")
    flight_number = st.text_input("Enter Flight Number for Search:")
    current_date = date.today()
    if st.button("Fetch Data"):
        if passenger_id and flight_number:
            data = fetch_passenger_data1(passenger_id, flight_number)
            if data:
                if data[0]["flight_date"] > current_date:
                    st.subheader("Current Passenger Details")
                    df = pd.DataFrame(data)
                    st.dataframe(df)
                else:
                    st.warning("Data can only be updated till the day before the flight leaves.")
            else:
                st.warning("No data found for the given Passenger ID and Flight Number.")
        else:
            st.error("Please provide both Passenger ID and Flight Number.")

    data = fetch_passenger_data1(passenger_id, flight_number)
    if data and data[0]["flight_date"] > current_date:
        st.subheader("Update Passenger Details")
        name = st.text_input("Enter New Name:")
        gender = st.radio("Choose Your Gender:", ["Male", "Female", "Other"])
        age = st.number_input("Enter New Age:", min_value=0, step=1)
        inflight_food = st.text_input("Enter New Inflight Food Preference:")

        if st.button("Update Data"):
            if passenger_id and flight_number and name and gender and age and inflight_food:
                update_passenger_data(passenger_id, flight_number, name, gender, age, inflight_food)
                updated_data = display_updated_passenger_data(passenger_id, flight_number)
                if updated_data:
                    st.subheader("Updated Passenger Details")
                    updated_df = pd.DataFrame(updated_data)
                    st.dataframe(updated_df)
                else:
                    st.warning("Failed to fetch updated data.")
            else:
                st.error("Please fill out all fields and provide Passenger ID and Flight Number.")

# Show previous Bookings of the user
elif st.session_state.page == "Your Bookings":
    st.title("Your Bookings")
    sidebar()
    db_connection = connect_to_db()
    cursor = db_connection.cursor(dictionary=True)
    query = "SELECT * FROM passenger_details where email = %s"
    cursor.execute(query, (st.session_state.email,))
    records = cursor.fetchall()
    db_connection.close()
    if records:
        df = pd.DataFrame(records)
        st.dataframe(df)
    else:
        st.success("No Previous Booking.")

# Feedback
elif st.session_state.page == 'Feedback and Queries':
    st.title('Feedback and Queries')
    sidebar()
    feed = st.text_area('Enter your Feedback or Query:',height=200)
    if st.button('Send'):
        if feed.strip():
            db_connection = connect_to_db()
            cursor = db_connection.cursor(dictionary=True)
            query = "INSERT INTO feedbacks values(%s,%s)"
            cursor.execute(query, (st.session_state.email,feed))
            db_connection.commit()
            db_connection.close()
            st.success("Your message has been uploaded. Please wait for our reply. THANK YOU :)")
        else:
            st.error("Message cannot be empty. Please enter a valid message.")
            
# User Account
elif st.session_state.page == 'Account':
    sidebar()
    data = fetch_passenger_data()
    st.title('Your Account Details')
    st.write("Username :",data["username"])
    st.write("Password :",data["password"])
    st.write("Email ID :",data["email"])

# Info
elif st.session_state.page == 'About':
    sidebar()
    st.title('About our Airline')
    st.write('''Welcome aboard our airline, where innovation meets exceptional service. Founded with a vision to redefine air travel, we are committed to providing passengers with seamless, comfortable, and safe journeys across the skies. 
    Our modern fleet connects both domestic and international destinations, ensuring efficiency and reliability in every flight. Guided by the core values of excellence, hospitality, and sustainability, our airline aims to deliver a superior
    travel experience. From the moment passengers step onboard, they are greeted with world-class amenities and a dedicated crew ready to cater to their every need. As a student-led project by Mithilesh.V, Sanjai.A, and HariPriyan.K,
    this initiative represents our shared passion for aviation and customer-centric innovation, showcasing a vision for an airline that truly puts passengers first.''')

# Rules
elif st.session_state.page == 'Rules':
    sidebar()
    st.title("Rules and Regulations")
    tabs = st.tabs(["Baggage Rules", "Check-In Rules", "Boarding Rules", "In-Flight Rules"])
    with tabs[0]:
        st.header("Baggage Rules")
        st.subheader("Cabin Baggage:")
        st.write("""
        - Passengers are allowed **1 piece of cabin baggage** weighing a maximum of **7 kg**.
        - The size of cabin baggage should not exceed **55 cm x 40 cm x 20 cm**.
        - Items like laptops, handbags, and small backpacks are permitted in addition to the cabin baggage.
        """)
        st.subheader("Checked-In Baggage:")
        st.write("""
        - **Economy Class/Premium Economy Class**: Passengers can carry up to **15 kg** of checked-in baggage for domestic flights and **20 kg** for international flights.
        - **Business Class/First Class**: Passengers are allowed up to **30 kg** of checked-in baggage.
        - Any excess baggage will incur additional charges.
        """)
        st.subheader("Prohibited Items:")
        st.write("""
        - Sharp objects, flammable items, explosives, and restricted liquids are not allowed in carry-on baggage.
        - Checked baggage cannot include power banks, lithium batteries, or valuables like jewelry.
        """)
        st.subheader("Special Baggage:")
        st.write("""
        - Musical instruments, sports equipment, and fragile items may require special handling and additional fees.
        - Advanced notice is required for oversized baggage.
        """)

    # Check-In Rules
    with tabs[1]:
        st.header("Check-In Rules")
        st.subheader("Online Check-In:")
        st.write("""
        - Online check-in opens **48 hours** and closes **2 hours** before departure for domestic flights.
        - For international flights, online check-in closes **3 hours** before departure.
        """)
        st.subheader("Airport Check-In:")
        st.write("""
        - Passengers should arrive at the airport **2 hours prior** for domestic flights and **3 hours prior** for international flights.
        - Check-in counters close **45 minutes** before departure for domestic flights and **60 minutes** before departure for international flights.
        """)
        st.subheader("Documents Required:")
        st.write("""
        - **Domestic Flights**: Government-issued photo ID (e.g., Aadhar, Passport, Driving License).
        - **International Flights**: Passport, visa (if applicable), and any necessary travel permits.
        """)
        st.subheader("Special Assistance:")
        st.write("""
        - Passengers requiring wheelchair assistance or traveling with infants must notify the airline at least **24 hours** prior to departure.
        """)

    # Boarding Rules
    with tabs[2]:
        st.header("Boarding Rules")
        st.subheader("Boarding Time:")
        st.write("""
        - Boarding gates open **60 minutes** before departure for international flights and **30 minutes** before domestic flights.
        - Boarding gates close **15 minutes** before departure for all flights.
        """)
        st.subheader("Priority Boarding:")
        st.write("""
        - Priority boarding is available for Business Class passengers, families with infants, and senior citizens.
        - Passengers with connecting flights are requested to inform the ground staff for assistance.
        """)
        st.subheader("Gate Information:")
        st.write("""
        - Check your boarding pass or airport screens for updated gate information.
        - Failure to report at the gate before closure may result in denied boarding.
        """)
        st.subheader("Prohibited Behavior:")
        st.write("""
        - Passengers displaying aggressive or intoxicated behavior will not be allowed to board the flight.
        """)

    # In-Flight Rules
    with tabs[3]:
        st.header("In-Flight Rules")
        st.subheader("Electronic Devices:")
        st.write("""
        - Mobile phones and electronic devices must be in **airplane mode** during the flight.
        - Use of larger electronics like laptops and tablets is permitted during cruising but not during take-off or landing.
        """)
        st.subheader("Seatbelt:")
        st.write("""
        - Passengers must wear seatbelts when the seatbelt sign is illuminated.
        - Infants must be secured with provided infant belts.
        """)
        st.subheader("Smoking:")
        st.write("""
        - SHM Airlines follows a strict **no-smoking policy** on all flights, including e-cigarettes.
        """)
        st.subheader("Food and Beverages:")
        st.write("""
        - Only food and drinks provided by the airline are permitted onboard.
        - Alcohol consumption is restricted to beverages served by the cabin crew.
        """)
