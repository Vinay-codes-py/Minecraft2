import streamlit as st
import streamlit.components.v1 as components
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="Streamlit 3D Voxel Sandbox",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Application Header & Description
st.title("⛏️ 3D Voxel Sandbox (Minecraft Clone)")
st.markdown("""
Welcome to the Procedural 3D Voxel Sandbox! This application embeds a fully custom WebGL engine built entirely with **Three.js** and **JavaScript**, served effortlessly by **Streamlit**. 

### 🎮 How to Play
- **Movement:** `W`, `A`, `S`, `D` keys.
- **Jump:** `Spacebar`.
- **Look Around:** Move your mouse (Pointer Lock).
- **Mine Block:** `Left Mouse Click`.
- **Place Block:** `Right Mouse Click`.
- **Exit Controls:** Press `ESC` to free your mouse pointer.

*Note: All textures, lighting, player models, and physics are generated procedurally in code without external assets.*
""")

# Load and embed the Three.js HTML file
def load_html_engine():
    html_file_path = "index.html"
    
    if os.path.exists(html_file_path):
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        st.markdown("---")
        # Render HTML component with disabled scrolling to lock the view
        components.html(html_content, height=800, scrolling=False)
    else:
        st.error(f"⚠️ Error: `{html_file_path}` not found in the current directory. Please ensure both files are in the same folder.")

# Execute Loader
load_html_engine()

# Tech Stack footer
st.markdown("""
---
**Tech Stack:** `Streamlit` (Python Web Framework), `Three.js` (WebGL 3D Rendering), `HTML5/CSS3` (DOM Overlays & Styling).
""")