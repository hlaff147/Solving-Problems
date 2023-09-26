import gzip
import base64
import io

def zip_and_encode(input_string):
    # 1. Compacta a string usando gzip
    buffer = io.BytesIO()
    with gzip.GzipFile(fileobj=buffer, mode="w") as f:
        f.write(input_string.encode("utf-8"))
    compressed_data = buffer.getvalue()

    # 2. Converte a string compactada para base64
    base64_encoded = base64.b64encode(compressed_data)
    return base64_encoded.decode("utf-8")

def save_to_txt(data, filename):
    with open(filename, "w") as file:
        file.write(data)

def read_from_txt(filename):
    with open(filename, "r") as file:
        return file.read()

# Lendo o conteúdo do arquivo input.txt
input_filename = "input.txt"
data = read_from_txt(input_filename)

# Compactando e codificando o conteúdo em base64
result = zip_and_encode(data)

# Salvando o resultado em um arquivo txt
output_filename = "output.txt"
save_to_txt(result, output_filename)
print(f"Resultado salvo em {output_filename}")
