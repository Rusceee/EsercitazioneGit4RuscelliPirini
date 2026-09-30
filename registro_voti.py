class RegistroVoti:
    """Gestisce i voti associati a ciascuno studente."""

    def __init__(self):
        self._voti = {}

    def aggiungi_voto(self, nome_studente: str, voto: float) -> None:
        if not isinstance(nome_studente, str) or not nome_studente.strip():
            raise ValueError("Il nome dello studente non può essere vuoto.")
        if isinstance(voto, bool) or not isinstance(voto, (int, float)):
            raise ValueError("Il voto deve essere un numero tra 0 e 10.")
        if not 0 <= voto <= 10:
            raise ValueError("Il voto deve essere un numero tra 0 e 10.")

        self._voti.setdefault(nome_studente.strip(), []).append(float(voto))

    def voti_studente(self, nome_studente: str) -> list[float]:
        return list(self._voti.get(nome_studente.strip(), []))

    def media_studente(self, nome_studente: str) -> float:
        voti = self.voti_studente(nome_studente)
        if not voti:
            raise ValueError(f"Nessun voto registrato per {nome_studente}.")
        return sum(voti) / len(voti)