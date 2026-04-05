#!/bin/bash
# =============================================================================
# run_pilot.sh — Pilot AODV vs OLSR (9-node linear chain)
# Executa duas simulacoes e imprime sumario basico
# =============================================================================

set -euo pipefail

BASE=/mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH
MESHSIM=$BASE/MeshSim/build/sim/mesh_sim
NS3_LIB=$BASE/ns-3-dev/build/lib
PILOT_DIR=$BASE/experiments/pilot_100_aodv_olsr

MESH_SIZE=9
STA_SIZE=9
DURATION=400   # 90s warm-up + 300s de medição

# --- Validacoes ---
if [ ! -f "$MESHSIM" ]; then
    echo "ERRO: mesh_sim nao encontrado em $MESHSIM"
    echo "  Compile primeiro: cd MeshSim/build && make -j8"
    exit 1
fi

export LD_LIBRARY_PATH=$NS3_LIB:${LD_LIBRARY_PATH:-}

echo "============================================="
echo " Pilot: AODV vs OLSR — cadeia linear 9 nos"
echo " meshSize=$MESH_SIZE  staSize=$STA_SIZE  duration=${DURATION}s"
echo "============================================="

# --- Criar diretorios de saida ---
mkdir -p "$PILOT_DIR/out_AODV"
mkdir -p "$PILOT_DIR/out_OLSR"

# --- Rodar AODV ---
echo ""
echo "[1/2] Rodando AODV..."
START=$(date +%s)
"$MESHSIM" \
    --meshSize=$MESH_SIZE \
    --staSize=$STA_SIZE \
    --simDuration=$DURATION \
    "$PILOT_DIR/config_AODV_seed42" \
    "$PILOT_DIR/out_AODV"
END=$(date +%s)
echo "      AODV concluido em $((END-START))s de CPU"

# --- Rodar OLSR ---
echo ""
echo "[2/2] Rodando OLSR..."
START=$(date +%s)
"$MESHSIM" \
    --meshSize=$MESH_SIZE \
    --staSize=$STA_SIZE \
    --simDuration=$DURATION \
    "$PILOT_DIR/config_OLSR_seed43" \
    "$PILOT_DIR/out_OLSR"
END=$(date +%s)
echo "      OLSR concluido em $((END-START))s de CPU"

# --- Sumario rapido ---
echo ""
echo "============================================="
echo " Sumario dos resultados"
echo "============================================="
for PROTO in AODV OLSR; do
    OUT="$PILOT_DIR/out_$PROTO"
    echo ""
    echo "--- $PROTO ---"
    echo "  Arquivos gerados:"
    ls "$OUT/"
    # Mostrar ultima linha de cada trace-app-rx (bytes totais recebidos)
    for f in "$OUT"/trace-app-rx-*.txt; do
        [ -f "$f" ] || continue
        TAG=$(grep "# tags_tx" "$f" | head -1 | awk '{print $NF}')
        RXIP=$(grep "# tag_rx" "$f" | head -1 | awk '{print $NF}')
        LAST=$(tail -1 "$f")
        TIME_US=$(echo $LAST | awk '{print $1}')
        BYTES=$(echo $LAST | awk '{print $2}')
        TIME_S=$(echo "scale=1; $TIME_US / 1000000" | bc)
        echo "  Conexao $TAG -> $RXIP: ${BYTES} bytes em ${TIME_S}s"
    done
done

echo ""
echo "Para analise completa, execute:"
echo "  python3 $PILOT_DIR/analyze_pilot.py"
