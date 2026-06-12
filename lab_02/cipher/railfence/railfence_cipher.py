class RailFenceCipher:
    def __init__(self):
        pass
    
    def rail_fence_encrypt(self, plain_text, num_rails):
        # Lọc bỏ số và khoảng trắng (chỉ giữ chữ cái)
        clean_text = "".join([c for c in plain_text if c.isalpha()])
        
        if num_rails < 2:
            return clean_text
            
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1
        for char in clean_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Lọc bỏ số và khoảng trắng
        clean_cipher = "".join([c for c in cipher_text if c.isalpha()])
        
        if num_rails < 2:
            return clean_cipher
            
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1
        
        for _ in range(len(clean_cipher)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1 
            rail_index += direction
            
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(clean_cipher[start:start + length])
            start += length 
        plain_text = ""
        rail_index = 0 
        direction = 1
        
        for _ in range(len(clean_cipher)):
            plain_text += rails[rail_index][0]
            rails[rail_index] = rails[rail_index][1:]
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        return plain_text