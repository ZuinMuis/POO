import pytest

from paciente import Paciente


def test_paciente_creates_valid_instance():
    p = Paciente("11.111.111-1", "Miguel Latos", 50, "Fonasa")

    assert p.rut == "11.111.111-1"
    assert p.nombre == "Miguel Latos"
    assert p.edad == 50
    assert p.prevision == "Fonasa"


def test_paciente_rejects_invalid_prevision():
    with pytest.raises(ValueError):
        Paciente("11.111.111-1", "Miguel Latos", 50, "Seguro")


def test_paciente_str_contains_key_details():
    p = Paciente("22.222.222-2", "Luis Arriagada", 40, "Isapre")

    text = str(p)
    assert "RUT: 22.222.222-2" in text
    assert "Nombre: Luis Arriagada" in text
    assert "Edad: 40" in text
    assert "Prevision: Isapre" in text
