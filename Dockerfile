# Use a imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo app.py para o contêiner
COPY app.py .

# Instale as dependências (Flask)
RUN pip install Flask

# Exponha a porta 5000 (a mesma usada pelo Flask)
EXPOSE 5000

# Comando de inicialização da aplicação
CMD ["python", "app.py"]