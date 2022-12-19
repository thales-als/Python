from datetime import datetime, timedelta


class Datas:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def formata_data(self):
        data_hora = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_hora

    def mes_cadastro(self):
        meses_do_ano = [
            ".", "Janeiro", "Fevereiro", "Março",
            "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro",
            "Outubro", "Novembro", "Dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month
        return f"Mês {mes_cadastro}, {meses_do_ano[mes_cadastro]}"

    def dia_semana(self):
        dia_semana_lista = [
            "Segunda-Feira",
            "Terça-Feira",
            "Quarta-Feira",
            "Quinta-Feira",
            "Sexta-Feira",
            "Sábado",
            "Domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro
