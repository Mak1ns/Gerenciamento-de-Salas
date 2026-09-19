from pathlib import Path

import sqlite3
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "reservas.db"


def conectar():
    return sqlite3.connect(DB_PATH)

def criar_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            tipo TEXT NOT NULL,
            departamento TEXT DEFAULT 'Geral'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS salas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            capacidade INTEGER,
            computadores INTEGER,
            projetor BOOLEAN,
            caixa_som BOOLEAN,
            status TEXT DEFAULT 'Ativa'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            professor_id INTEGER,
            sala_id INTEGER,
            data TEXT,
            horario_inicio TEXT,
            horario_fim TEXT,
            finalidade TEXT,
            status TEXT DEFAULT 'Confirmada',
            FOREIGN KEY (professor_id) REFERENCES usuarios(id),
            FOREIGN KEY (sala_id) REFERENCES salas(id)
        )
    """)

    conexao.commit()
    conexao.close()

def criar_usuarios_iniciais():
    conexao = conectar()
    cursor = conexao.cursor()  

    usuarios = [
        ("Administrador Geral", "admin@unisapiens.edu", "1234", "Administrador", "Gestão de TI"),
        ("Prof. Átila", "atila@unisapiens.edu", "1234", "Professor", "Engenharia do Conhecimento"),
        ("Profa. Mariana Costa", "mariana.costa@unisapiens.edu", "1234", "Professor", "Ciência da Computação")
    ]

    for u in usuarios:
        try:
            cursor.execute("INSERT INTO usuarios (nome, email, senha, tipo, departamento) VALUES (?, ?, ?, ?, ?)", u)
        except sqlite3.IntegrityError:
            pass

    conexao.commit()
    conexao.close()

def criar_salas_iniciais():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM salas")
    if cursor.fetchone()[0] == 0:
        salas = [
            ("Sala 101", 40, 0, True, False, "Ativa"),
            ("Laboratório de Informatica", 30, 30, True, True, "Ativa"),
            ("Sala Nova york", 20, 0, False, False, "Ativa"),
            ("Sala de Reuniões", 15, 0, True, True, "Ativa"),
            ("Laboratório de Robótica", 25, 10, True, True, "Ativa")
        ]
        cursor.executemany("INSERT INTO salas (nome, capacidade, computadores, projetor, caixa_som, status) VALUES (?, ?, ?, ?, ?, ?)", salas)

    conexao.commit()
    conexao.close()


if __name__ == "__main__":
    criar_banco()
    criar_usuarios_iniciais()
    print(f"Banco criado/atualizado em: {DB_PATH}")
