from pulp import *

# 1. Definisikan Masalah
prob = LpProblem("Optimalisasi Distribusi Aset IT SBA", LpMinimize)

# 2. Variabel Keputusan (Integer)
Y_A = LpVariable("Y_Pemasok_A", lowBound=0, cat='Integer')
Y_B = LpVariable("Y_Pemasok_B", lowBound=0, cat='Integer')

X_1 = LpVariable("X_Bintaro", lowBound=0, cat='Integer')
X_2 = LpVariable("X_Meruya", lowBound=0, cat='Integer')
X_3 = LpVariable("X_Cikande", lowBound=0, cat='Integer')

# 3. Fungsi Tujuan (Minimalisasi Biaya Total Z)
Biaya_Beli = (9750000 * Y_A) + (9675000 * Y_B)
Biaya_Transp = (120000 * X_1) + (270000 * X_2) + (600000 * X_3)

prob += Biaya_Beli + Biaya_Transp, "Total_Biaya_Z"

# 4. Kendala
# Kendala Kebutuhan Cabang (Demand)
prob += X_1 >= 50, "Kebutuhan_Bintaro"
prob += X_2 >= 65, "Kebutuhan_Meruya"
prob += X_3 >= 45, "Kebutuhan_Cikande"

# Kendala Kapasitas Gudang (Supply)
prob += X_1 + X_2 + X_3 <= 180, "Kapasitas_Gudang_Pusat"

# Kendala Keseimbangan Aliran (Flow Balance)
prob += (Y_A + Y_B) == (X_1 + X_2 + X_3), "Keseimbangan_Pengadaan_Distribusi"

# 5. Solusi
# prob.solve()
# print("Status:", LpStatus[prob.status])
# print("Biaya Minimum Total:", value(prob.objective))