from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():

    data = {
        "Kategori": [
            "Makan",
            "Transport",
            "Internet",
            "Hiburan",
            "Lain-lain"
        ],
        "Pengeluaran": [
            500000,
            200000,
            150000,
            250000,
            100000
        ]
    }

    df = pd.DataFrame(data)

    total = df["Pengeluaran"].sum()
    rata = df["Pengeluaran"].mean()
    maksimum = df["Pengeluaran"].max()
    minimum = df["Pengeluaran"].min()

    return f"""
    <h1>Analisa Pengeluaran Mahasiswa</h1>

    <p>Total Pengeluaran : Rp {total:,}</p>

    <p>Rata-rata Pengeluaran : Rp {rata:,.0f}</p>

    <p>Pengeluaran Tertinggi : Rp {maksimum:,}</p>

    <p>Pengeluaran Terendah : Rp {minimum:,}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
