from flask import Flask, render_template, request, json

# Import các class xử lý mã hóa
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayFairCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher

app = Flask(__name__)

# ==================== HOME PAGE ====================
@app.route("/")
def home():
    return render_template('index.html')

# ==================== CAESAR CIPHER ====================
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    
    return render_template('result.html', 
                           cipher_type="Caesar Cipher",
                           action_type="Encryption",
                           input_text=text, 
                           key=key, 
                           output_text=encrypted_text)

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    
    return render_template('result.html', 
                           cipher_type="Caesar Cipher",
                           action_type="Decryption",
                           input_text=text, 
                           key=key, 
                           output_text=decrypted_text)

# ==================== PLAYFAIR CIPHER ====================
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/encrypt_playfair", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain'] 
    
    Playfair = PlayFairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    encrypted_text = Playfair.playfair_encrypt(text, matrix)
    
    return render_template('result.html', 
                           cipher_type="Playfair Cipher",
                           action_type="Encryption",
                           input_text=text, 
                           key=key, 
                           output_text=encrypted_text,
                           matrix=matrix) # Thêm dòng này để gửi ma trận sang web

@app.route("/decrypt_playfair", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    
    Playfair = PlayFairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    decrypted_text = Playfair.playfair_decrypt(text, matrix)
    
    return render_template('result.html', 
                           cipher_type="Playfair Cipher",
                           action_type="Decryption",
                           input_text=text, 
                           key=key, 
                           output_text=decrypted_text,
                           matrix=matrix)

# ==================== VIGENERE CIPHER ====================
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/encrypt_vigenere", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)
    
    return render_template('result.html', 
                           cipher_type="Vigenère Cipher",
                           action_type="Encryption",
                           input_text=text, 
                           key=key, 
                           output_text=encrypted_text)

@app.route("/decrypt_vigenere", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)
    
    return render_template('result.html', 
                           cipher_type="Vigenère Cipher",
                           action_type="Decryption",
                           input_text=text, 
                           key=key, 
                           output_text=decrypted_text)

# ==================== RAIL FENCE CIPHER ====================
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/encrypt_railfence", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    RailFence = RailFenceCipher()
    encrypted_text = RailFence.rail_fence_encrypt(text, key)
    
    return render_template('result.html', 
                           cipher_type="Rail Fence Cipher",
                           action_type="Encryption",
                           input_text=text, 
                           key=key, 
                           output_text=encrypted_text)

@app.route("/decrypt_railfence", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    RailFence = RailFenceCipher()
    decrypted_text = RailFence.rail_fence_decrypt(text, key)
    
    return render_template('result.html', 
                           cipher_type="Rail Fence Cipher",
                           action_type="Decryption",
                           input_text=text, 
                           key=key, 
                           output_text=decrypted_text)

# ==================== MAIN ====================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)