#!/bin/bash
# =============================================================================
# run_all_experiments.sh — Roda TODOS os experimentos AODV vs OLSR
#
# Topologias:
#   1. chain-9   (cadeia linear  9 nos)  duration=400s
#   2. grid-25   (grid 5x5      25 nos)  duration=500s
#   3. random-50 (aleatorio     50 nos)  duration=600s
#
# Uso:
#   ./run_all_experiments.sh             # roda tudo
#   ./run_all_experiments.sh --dry-run   # apenas mostra os comandos
#   ./run_all_experiments.sh chain-9     # roda so a topologia indicada
#   ./run_all_experiments.sh grid-25 random-50  # roda subset
# =============================================================================

set -euo pipefail

BASE=/mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH
MESHSIM=$BASE/MeshSim/build/sim/mesh_sim
NS3_LIB=$BASE/ns-3-dev/build/lib
EXPS=$BASE/experiments

# --- Parsear argumentos ---
DRY_RUN=0
RUN_TOPOLOGIES=()

for arg in "$@"; do
    case "$arg" in
        --dry-run) DRY_RUN=1 ;;
        chain-9|grid-25|random-50) RUN_TOPOLOGIES+=("$arg") ;;
        *) echo "Argumento desconhecido: $arg"; exit 1 ;;
    esac
done

# Sem argumento de topologia = roda tudo
if [ ${#RUN_TOPOLOGIES[@]} -eq 0 ]; then
    RUN_TOPOLOGIES=("chain-9" "grid-25" "random-50")
fi

# --- Validacoes ---
if [ ! -f "$MESHSIM" ]; then
    echo "ERRO: mesh_sim nao encontrado: $MESHSIM"
    echo "  Compile: cd $BASE/MeshSim/build && make -j\$(nproc)"
    exit 1
fi

export LD_LIBRARY_PATH=$NS3_LIB:${LD_LIBRARY_PATH:-}


# =============================================================================
# Funcao auxiliar: rodar uma simulacao
# =============================================================================
run_sim() {
    local LABEL=$1
    local CONFIG=$2
    local OUT=$3
    local MESH_SIZE=$4
    local STA_SIZE=$5
    local DURATION=$6

    echo ""
    echo "┌─ [$(date +%H:%M:%S)] $LABEL"
    echo "│  config:   $(basename $CONFIG)"
    echo "│  saida:    $(realpath --relative-to=$BASE $OUT)"
    echo "│  params:   meshSize=$MESH_SIZE  staSize=$STA_SIZE  duration=${DURATION}s"

    if [[ $DRY_RUN -eq 1 ]]; then
        echo "│  [DRY RUN] $MESHSIM --meshSize=$MESH_SIZE --staSize=$STA_SIZE"
        echo "│             --simDuration=$DURATION $CONFIG $OUT"
        echo "└─ (pulado)"
        return 0
    fi

    if [ ! -d "$CONFIG" ]; then
        echo "└─ ERRO: config nao encontrada: $CONFIG"
        echo "   Execute: python3 $EXPS/generate_all_configs.py"
        return 1
    fi

    mkdir -p "$OUT"
    # Limpar resultados anteriores para evitar mistura de runs
    rm -f "$OUT"/*.xml "$OUT"/*.txt "$OUT"/*.pcap 2>/dev/null || true

    START=$(date +%s)
    "$MESHSIM" \
        --meshSize=$MESH_SIZE \
        --staSize=$STA_SIZE \
        --simDuration=$DURATION \
        "$CONFIG" \
        "$OUT"
    END=$(date +%s)

    ELAPSED=$((END - START))
    echo "└─ concluido em ${ELAPSED}s"
}


# =============================================================================
# Funcao: gerar configs se necessario
# =============================================================================
ensure_configs() {
    local NEED_GEN=0
    for topo in "${RUN_TOPOLOGIES[@]}"; do
        case "$topo" in
            grid-25)
                [ -d "$EXPS/grid_25nodes/config_AODV_seed100" ] || NEED_GEN=1 ;;
            random-50)
                [ -d "$EXPS/random_50nodes/config_AODV_seed200" ] || NEED_GEN=1 ;;
        esac
    done

    if [[ $NEED_GEN -eq 1 ]]; then
        echo ""
        echo ">>> Gerando configs (grid_25nodes, random_50nodes)..."
        python3 "$EXPS/generate_all_configs.py"
    fi
}


# =============================================================================
# Main
# =============================================================================
echo "======================================================"
echo "  AODV vs OLSR — Suite completa de experimentos"
echo "  Topologias: ${RUN_TOPOLOGIES[*]}"
if [[ $DRY_RUN -eq 1 ]]; then
    echo "  MODO: DRY RUN"
fi
echo "======================================================"

ensure_configs

TOTAL_START=$(date +%s)

# ── 1. chain-9 ────────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "chain-9"; then
    echo ""
    echo "━━━ Topologia 1/3: Cadeia Linear 9 nos ━━━━━━━━━━━━━"

    run_sim "chain-9  AODV" \
        "$EXPS/pilot_100_aodv_olsr/config_AODV_seed42" \
        "$EXPS/pilot_100_aodv_olsr/out_AODV" \
        9 9 400

    run_sim "chain-9  OLSR" \
        "$EXPS/pilot_100_aodv_olsr/config_OLSR_seed43" \
        "$EXPS/pilot_100_aodv_olsr/out_OLSR" \
        9 9 400
fi

# ── 2. grid-25 ────────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "grid-25"; then
    echo ""
    echo "━━━ Topologia 2/3: Grid 5x5 (25 nos) ━━━━━━━━━━━━━━"

    run_sim "grid-25  AODV" \
        "$EXPS/grid_25nodes/config_AODV_seed100" \
        "$EXPS/grid_25nodes/out_AODV" \
        25 25 500

    run_sim "grid-25  OLSR" \
        "$EXPS/grid_25nodes/config_OLSR_seed101" \
        "$EXPS/grid_25nodes/out_OLSR" \
        25 25 500
fi

# ── 3. random-50 ──────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "random-50"; then
    echo ""
    echo "━━━ Topologia 3/3: Random 50 nos ━━━━━━━━━━━━━━━━━━"

    run_sim "random-50 AODV" \
        "$EXPS/random_50nodes/config_AODV_seed200" \
        "$EXPS/random_50nodes/out_AODV" \
        50 50 600

    run_sim "random-50 OLSR" \
        "$EXPS/random_50nodes/config_OLSR_seed201" \
        "$EXPS/random_50nodes/out_OLSR" \
        50 50 600
fi

TOTAL_END=$(date +%s)
TOTAL=$((TOTAL_END - TOTAL_START))

echo ""
echo "======================================================"
echo "  Concluido em $((TOTAL/60))m $((TOTAL%60))s"
echo ""
echo "  Para analisar todos os resultados:"
echo "    python3 $EXPS/analyze_all.py"
echo ""
echo "  Para analisar so o piloto:"
echo "    python3 $EXPS/pilot_100_aodv_olsr/analyze_pilot.py"
echo "======================================================"
