import streamlit as st

st.header("Caesar Cipher")

def encrypt_decrypt(text, shift_keys, ifdecrypt):
    """
    Encrypts a text using Caesar Cipher with a list of shift keys.
    Args:
        text: The text to encrypt.
        shift_keys: A list of integers representing the shift values for each character.
        ifdecrypt: flag if decrypt or encrypt
    Returns:
        A string containing the encrypted text if encrypt and plain text if decrypt
    """
    result = ""
     
    if len(shift_keys)  <= 1 or len (shift_keys) > len(text):
        raise ValueError("Invalid shift keys length")
        
    for i, char in enumerate(text):
        shift_key = shift_keys[i % len(shift_keys)]
        
        if 32 <= ord(char) <= 125:
            new_ascii = ord(char) + shift_key if not ifdecrypt else ord(char) - shift_key
            while new_ascii > 125:
                new_ascii -= 94
            while new_ascii < 32:
                new_ascii += 94
            result += chr(new_ascii)
        else:
            result += char
        st.write(str(i) + " ", char, str(shift_key), result[i])
    return result

# Streamlit UI setup
text = st.text_input("Text")
shift_keys_str = st.text_input("Shift keys (space-separated)")
shift_keys = [int(key) for key in shift_keys_str.split()]

if st.button("Submit"):
    if not shift_keys:
        st.error("Please enter shift keys.")
    else:
        encrypted_text = encrypt_decrypt(text, shift_keys, False)
        decrypted_text = encrypt_decrypt(encrypted_text, shift_keys, True)

        st.write("----------")
        st.write("Text:", text)
        st.write("Shift keys:", shift_keys_str)
        st.write("Cipher:", encrypted_text)
        st.write("Decrypted text:", decrypted_text)

st.balloons()
st.snow()


    