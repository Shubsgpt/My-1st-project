import streamlit as st

# Title and Introduction
st.title("How Facebook Photo Upload Works: Backend Process")
st.markdown("""
### Introduction
This website explains the backend process involved in uploading a photo to Facebook and how it is displayed in the application.
""")

# Step 1: User Uploads Photo
st.header("Step 1: User Uploads Photo")
st.markdown("""
- **Client-Side Preparation**: User selects a photo, and it might be compressed or chunked.
- **Upload Request**: The photo is sent to Facebook’s server in chunks.
""")
st.image("https://via.placeholder.com/600x200", caption="User Uploading Photo")

# Step 2: Backend Processing During Upload
st.header("Step 2: Backend Processing During Upload")
st.markdown("""
- **Receiving Data**: The server receives the photo chunks and starts reassembly.
- **Temporary Storage**: Chunks are stored temporarily until the full photo is received.
""")
st.image("https://via.placeholder.com/600x200", caption="Backend Processing")

# Step 3: Post-Upload Processing
st.header("Step 3: Post-Upload Processing")
st.markdown("""
- **Image Processing**: The photo is resized, cropped, and analyzed.
- **Data Storage**: The photo is stored in a distributed system with replication.
""")
st.image("https://via.placeholder.com/600x200", caption="Image Processing and Storage")

# Step 4: Database and Metadata Management
st.header("Step 4: Database and Metadata Management")
st.markdown("""
- **Metadata Storage**: Information about the photo is stored in a database.
- **Linking with User Data**: The photo is linked to the user's profile and feed.
""")
st.image("https://via.placeholder.com/600x200", caption="Database Management")

# Step 5: Displaying the Photo
st.header("Step 5: Displaying the Photo")
st.markdown("""
- **Content Delivery Network (CDN)**: The photo is cached and served from the nearest server.
- **Rendering on the Application**: The photo is displayed based on the user's device and network conditions.
""")
st.image("https://via.placeholder.com/600x200", caption="Photo Rendering")

# Step 6: Monitoring and Logging
st.header("Step 6: Monitoring and Logging")
st.markdown("""
- **Error Handling**: The backend manages errors and retries.
- **User Feedback**: Users are notified of upload success or failure.
""")
st.image("https://via.placeholder.com/600x200", caption="Monitoring and Logging")

# Step 7: Post-Processing
st.header("Step 7: Post-Processing (Optional)")
st.markdown("""
- **Tagging and AI Analysis**: The photo is analyzed for tags and faces.
- **Archiving and Long-Term Storage**: Older photos are moved to long-term storage.
""")
st.image("https://via.placeholder.com/600x200", caption="Post-Processing")
