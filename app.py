import streamlit as st



def main():
    st.title("Amazon Dashboard")
    st.image("image.png")
    pbix_file_path = "dashboard.pbix"  # Replace with your .pbix file path
    with open(pbix_file_path, "rb") as file:
        pbix_bytes = file.read()
    st.download_button(
        label="Download .pbix file",
        data=pbix_bytes,
        file_name="amazon_dashboard.pbix",
        mime="application/octet-stream"
    )
    
    # Add GitHub and Medium blog links
    st.markdown("### Additional Resources")
    st.markdown("[GitHub Repository](https://github.com/Harshithvarma007/Spotify-Dashboard)")
    

if __name__ == "__main__":
    main()
