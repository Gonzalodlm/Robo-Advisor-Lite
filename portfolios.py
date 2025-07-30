# Carteras modelo muy simplificadas (pesos suman 1.0)

MODEL_PORTFOLIOS = {
    0: {  # Conservador
        "AGG": 0.60,  # iShares Core US Aggregate Bond
        "BIL": 0.20,  # Invesco Treasury 1-3 M
        "GLD": 0.10,  # SPDR Gold
        "VT": 0.10,   # Vanguard Total World Stock
    },
    1: {  # Moderado
        "AGG": 0.40,
        "VT": 0.35,
        "VNQ": 0.15,  # Vanguard REIT
        "GLD": 0.10,
    },
    2: {  # Balanceado
        "VT": 0.50,
        "AGG": 0.25,
        "VNQ": 0.15,
        "GLD": 0.10,
    },
    3: {  # Crecimiento
        "VT": 0.70,
        "QQQ": 0.15,  # Nasdaq 100
        "VNQ": 0.10,
        "AGG": 0.05,
    },
    4: {  # Agresivo
        "VT": 0.55,
        "QQQ": 0.25,
        "IEMG": 0.10,  # Mercados emergentes
        "ARKK": 0.10,  # Innovación disruptiva
    },
}
