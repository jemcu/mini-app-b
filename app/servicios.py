_PREGUNTAS = [
    {
        "id": 1,
        "texto": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": ["Marte", "Júpiter", "Saturno", "Venus"],
        "respuesta_correcta": 1,
    },
    {
        "id": 2,
        "texto": "¿Quién escribió Don Quijote de la Mancha?",
        "opciones": [
            "Federico García Lorca",
            "Miguel de Cervantes",
            "Lope de Vega",
            "Benito Pérez Galdós",
        ],
        "respuesta_correcta": 1,
    },
    {
        "id": 3,
        "texto": "¿Cuál es la capital de Japón?",
        "opciones": ["Kioto", "Osaka", "Tokio", "Nagoya"],
        "respuesta_correcta": 2,
    },
    {
        "id": 4,
        "texto": "¿Qué gas absorben principalmente las plantas durante la fotosíntesis?",
        "opciones": ["Oxígeno", "Nitrógeno", "Hidrógeno", "Dióxido de carbono"],
        "respuesta_correcta": 3,
    },
    {
        "id": 5,
        "texto": "¿En qué continente se encuentra Egipto?",
        "opciones": ["África", "Asia", "Europa", "América"],
        "respuesta_correcta": 0,
    },
]


def listar_preguntas():
    return [
        {
            "id": pregunta["id"],
            "texto": pregunta["texto"],
            "opciones": pregunta["opciones"].copy(),
        }
        for pregunta in _PREGUNTAS
    ]


def obtener_respuesta_correcta(pregunta_id: int) -> int | None:
    for pregunta in _PREGUNTAS:
        if pregunta["id"] == pregunta_id:
            return pregunta["respuesta_correcta"]
    return None
