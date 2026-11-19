from app import servicios


def test_lista_publica_tiene_formato_seguro():
    preguntas = servicios.listar_preguntas()

    assert len(preguntas) == 5
    for pregunta in preguntas:
        assert set(pregunta) == {"id", "texto", "opciones"}
        assert isinstance(pregunta["id"], int)
        assert pregunta["texto"]
        assert len(pregunta["opciones"]) == 4
        assert all(isinstance(opcion, str) and opcion for opcion in pregunta["opciones"])


def test_modificar_pregunta_devuelta_no_modifica_datos_en_memoria():
    preguntas = servicios.listar_preguntas()
    primera_opcion_original = preguntas[0]["opciones"][0]
    preguntas[0]["opciones"][0] = "Opción modificada"

    preguntas_actualizadas = servicios.listar_preguntas()
    assert preguntas_actualizadas[0]["opciones"][0] == primera_opcion_original


def test_id_inexistente_no_tiene_respuesta_correcta():
    assert servicios.obtener_respuesta_correcta(9999) is None
