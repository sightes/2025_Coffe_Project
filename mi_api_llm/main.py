from fastapi import FastAPI
from pydantic import BaseModel
from llama_cpp import Llama
from typing import List
import json
import psycopg2

def ejecutar_sql(query: str):
    conn = psycopg2.connect(
        dbname="granada",
        user="sebastianulloa",
        password="tu_tugimalo1contraseña",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()
    
    # Arma un texto tipo tabla
    resultados = [dict(zip(columns, row)) for row in rows]
    return resultados
app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

llm = Llama(model_path="./qwen2.5.gguf", n_ctx=5000)

@app.post("/chat")
async def chat_con_datos(req: PromptRequest):
    # Paso 1: traducir pregunta a consulta SQL (a mano o via prompt)
    if "clientes" in req.prompt.lower():
        query = "SELECT first_name, rut_number FROM beneficiaries limit 100;"
    else:
        return {"response": "No entendí qué buscar. Pregunta sobre 'clientes' o 'ventas'."}

    # Paso 2: ejecutar la consulta
    datos = ejecutar_sql(query)
    contexto = json.dumps(datos, indent=2)

    # Paso 3: crear prompt para el LLM
    prompt = f"""
Eres un asistente experto en datos administrativos que trabaja con la base de datos de beneficiarios del sistema Granada. Tu tarea es entregar respuestas concisas, claras y en español, usando únicamente la información proporcionada como contexto. No inventes datos. Si no sabes, responde "No tengo información suficiente".

Contexto extraído de la base de datos:

{contexto}

Pregunta del usuario: {req.prompt}
Respuesta:"""

    output = llm(prompt, max_tokens=req.max_tokens)
    return {"response": output["choices"][0]["text"]}